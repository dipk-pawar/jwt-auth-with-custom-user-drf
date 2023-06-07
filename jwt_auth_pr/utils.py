from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Util:
    @staticmethod
    def send_email(subject, recipient, message):
        message = Mail(
            from_email=settings.EMAIL_HOST_USER,
            to_emails=recipient,
            subject=subject,
            html_content=message,
        )

        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
