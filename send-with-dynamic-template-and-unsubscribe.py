# Standard Library
from typing import Union, List

# SendGrid
from sendgrid import SendGridAPIClient, Asm
from sendgrid.helpers.mail import Mail

# Dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")


def send_with_dynamic_template_and_unsubscribe(to_emails: Union[str, List[str]]):
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
    # Add the unsubscribe group id
    #
    unsubscribe_group_id = int(config.get("UNSUBSCRIBE_GROUP_ID"))
    message.asm = Asm(unsubscribe_group_id, [unsubscribe_group_id])
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

    send_with_dynamic_template_and_unsubscribe(config.get("TO_EMAIL"))
