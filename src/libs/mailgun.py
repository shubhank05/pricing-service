import os
from typing import List
from requests import Response, post
class MailgunException(Exception):
    def __init__(self, message:str):
        self.message = message
class Mailgun:

    FROM_TITLE = 'Pricing service'
    FROM_EMAIL = 'shubhank.sharma@mba.christuniversity.in'
    @classmethod
    def send_mail(cls, email: List[str], subject: str, text:str, html: str)-> Response:
        MAILGUN_API_KEY = os.environ.get('mailgun_api_key', None)
        MAILGUN_DOMAIN = os.environ.get('mailgun_domain', None)
        if MAILGUN_API_KEY is None:
            raise MailgunException('Failed to load Mailgun API Key')
        if MAILGUN_DOMAIN is None:
            raise MailgunException('Failed to load Mailgun Domain')
        response = post(
            f"{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})
        if response.status_code != 200:
            print(response.json())
            raise MailgunException('An error occured while sending e-mail')
        return response
