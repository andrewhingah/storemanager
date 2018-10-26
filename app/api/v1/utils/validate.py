import re

def verify_user_details(name):
    """check that user details are valid"""
    if len(name.strip()) == 0:
        return {"message":"username annot be empty"}, 400
    if len(name) < 3:
        return {"message":"Too short, please add more characters"}, 400
    if len(name) > 15:
        return 'Too long, please remove some characters', 400
    if name.isdigit():
        return {"message":"This cannot be digits only"}, 400

def validate_email(email):
    
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    if not re.match(email_regex, email):
        return {
                'Status': 'Error',
                'Message': 'Ooops! {} is not a valid email address'.format(email) }, 400