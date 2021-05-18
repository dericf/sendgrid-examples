# sendgrid-examples

## Set up your SendGrid account

1. Create a sendgrid account
2. Make sure you go through all the steps to set up a verified sender
3. Create a restricted API key and enable the needed permissions
4. Create an unsubscribe group
5. Create a dynamic template

## Running the examples locally

1. Clone the repository
2. Create a .env file with the following variables

```
SEND_GRID_API_KEY=<YOUR API KEY HERE>
FROM_EMAIL=<YOUR FROM EMAIL HERE>
TO_EMAIL=<YOUR TO EMAIL HERE>
UNSUBSCRIBE_GROUP_ID=<YOUR GROUP ID HERE>
DYNAMIC_TEMPLATE_ID=<YOUR DYNAMIC TEMPLATE ID HERE>
```

3. Create a virtual environment with `venv`:
   `python3 -m venv venv`
4. Activate the virtual environment:
   `source ./venv/bin/activate`
5. Install packages
   `pip install -r requirements.txt`
6. Run the desired example (e.g. `python send-basic.py`)
