# Standard Library
from typing import Union, List

# SendGrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")


def send_with_dynamic_template(to_emails: Union[str, List[str]]):
    #
    # Build Sendgrid Mail Object
    #
    message = Mail(from_email=config.get("FROM_EMAIL"),
                   to_emails=to_emails
                   )
    #
    # Set the dynamic template id
    #
    message.template_id = config.get("DYNAMIC_TEMPLATE_ID")
    #
    # Add any dynamic template fields
    #
    message.dynamic_template_data = {
        "test_field": "This is a dynamic field",
        "subject_field": "dynamic subject"
    }
    #
    # Send the email
    #
    try:
        sg = SendGridAPIClient(config.get("SEND_GRID_API_KEY"))
        response = sg.send(message)
        print("Success! Email was sent.")

    except Exception as e:
        print("error sending email", e)


if __name__ == "__main__":

    send_with_dynamic_template(config.get("TO_EMAIL"))
