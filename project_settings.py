import logging
import boto3

from socket import gethostname
from django.utils.functional import classproperty
from utils import get_env_var
from exceptions import MissingCredentialError

logger = logging.getLogger(__name__)

class Project_Settings:
    
    ####################
    # General Settings #
    ####################
    @classproperty
    def enable_debug_logging(cls):
        return True

    @classproperty
    def use_env_for_credentials(cls):
        return get_env_var("USE_ENV_FOR_CREDENTIALS", False) == "1"

    @classproperty
    def django_server_enable_ssl(cls):
        return get_env_var("DJANGO_SERVER_ENABLE_SSL",False) == "1"

    @classproperty
    def django_secret_key(cls):
        return cls.get_secure_config_value("DJANGO_SERVER_SECRET_KEY")
    
    @classproperty
    def django_server_debug_mode(cls):
        if get_env_var("DJANGO_SERVER_DEBUG_MODE",False) == "1":
            logger.warning("!!! DEBUG MODE IS SET TO TRUE. TURN THIS OFF IN PRODUCTION!!!")
        return get_env_var("DJANGO_SERVER_DEBUG_MODE",False) == "1"

    @classproperty
    def django_server_tz(cls):
        return get_env_var("DJANGO_SERVER_TIMEZONE")
        
    @classproperty
    def allowed_hosts(cls):
        hosts = get_env_var("ALLOWED_HOSTS")
        return hosts.split(',')

    ###################
    # Django Settings #
    ###################
    @classproperty
    def django_server_host_name(cls):
        return gethostname()

    #####################
    # Database Settings #
    #####################
    @classproperty
    def db_name(cls):
        return cls.get_secure_config_value("GIDAI_DB_DATABASE")
    
    @classproperty
    def db_username(cls):
        return cls.get_secure_config_value("GIDAI_DB_USERNAME")
        
    @classproperty
    def db_pwd(cls):
        return cls.get_secure_config_value("GIDAI_DB_PASSWORD")
        
    @classproperty
    def db_host(cls):
        return cls.get_secure_config_value("GIDAI_DB_HOSTNAME")
        
    @classproperty
    def db_port(cls):
        return cls.get_secure_config_value("GIDAI_DB_PORT")


    #################
    # Secure Method #
    #################
    @classmethod
    def get_secure_config_value(cls, key):
        if cls.use_env_for_credentials:
            return get_env_var(key)
        else:
            # Determine if the underscores need to be converted to dashes
            #logger.info('Retrieval from AWS KMS not set up')
            #secret_key = key.replace("_","-")
            #return cls.get_required_secret(secret_key)

            return ''

    @classmethod
    def get_required_secret(cls,key):
        return ""

    
    ##################
    # AWS MKS config #
    ##################

    #########################
    # AWS S3 Helper Methods #
    #########################
    @classproperty
    def aws_s3_resource(cls):
        return boto3.resource('s3')

    @classproperty
    def aws_s3_bucket(cls,bucket_name):
        return cls.aws_s3_resource.Bucket(bucket_name)

    ###################
    # Image base urls #
    ###################
    @classproperty
    def user_avatar_base(cls):
        return get_env_var("CDN_USER_AVATAR_BASE_URL")
        
    @classproperty
    def event_image_base(cls):
        return get_env_var("CDN_EVENT_IMAGE_BASE_URL")

    ###################
    # Mailer Settings #
    ###################
    @classproperty
    def email_sender(cls):
        return get_env_var("DEFAULT_EMAIL_SENDER")

    @classproperty
    def sendgrid_api_key(cls):
        return cls.get_secure_config_value("SENDGRID_API_KEY")