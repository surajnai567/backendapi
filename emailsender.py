import threading
from project_settings import Project_Settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailSender(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    @classmethod
    def instance(cls, key):
        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls(key)

        # return the singleton instance
        return cls.__singleton_instance

    def __init__(self, key):
        self.key = key
        self.sg = SendGridAPIClient(key)

    def send(self, toemail, otp):
        message = Mail(
            from_email=Project_Settings.email_sender,
            #from_email='surajnai567@gmail.com',
            #from_email='siying0529@gmail.com',
            to_emails='{}'.format(toemail),
            subject='Gidai password reset',
            #TODO: Add an html page for emal rendering
            html_content='<strong>Here is the otp for setting the password {}</strong>'.format(otp),
        )

        try:
            response = self.sg.send(message)
            print(response.status_code)
        except Exception as e:
            print(e)


