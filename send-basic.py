# Standard Library
from typing import Union, List

# SendGrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")


def send_basic_email(to_emails: Union[str, List[str]], subject: str, html_content: str):
    #
    # Build Sendgrid Mail Object
    #
    message = Mail(from_email=config.get("FROM_EMAIL"),
                   to_emails=to_emails,
                   subject=subject,
                   html_content=html_content
                   )
    try:
        sg = SendGridAPIClient(config.get("SEND_GRID_API_KEY"))
        response = sg.send(message)
        print("Success! Email was sent.")

    except Exception as e:
        print("error sending email", e)


if __name__ == "__main__":

    html_content = """
    <html>
    <body>
    <h1>This is a test...</h1>
    </body>
    </html>
    """

    send_basic_email(config.get("TO_EMAIL"), "Testing Examples", html_content)
