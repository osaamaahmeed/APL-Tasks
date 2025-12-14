import re

def validate_emails(email_list):
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.(com|org|edu)$"

    for email in email_list:
        if re.match(pattern, email):
            print(f"{email} is Valid")
        else:
            print(f"{email} is Invalid")

emails = ["username@example.com", "bad-email", "test@domain.org"]
validate_emails(emails)