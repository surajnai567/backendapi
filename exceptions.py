######################
# General Exceptions #
######################

class BaseException(Exception):
    pass

class MissingEnvVarError(BaseException):
    pass

class MissingCredentialError(BaseException):
    pass