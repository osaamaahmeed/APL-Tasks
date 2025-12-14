import re

def validate_phone_number(phoneNumber):
    pattern = r"^(\+1-)?(\d{3}-)?\d{3}-\d{4}$"
    if (re.match(pattern, phoneNumber)):
        print(f"{phoneNumber} is Valid")
    else:
        print(f"{phoneNumber} is Invalid")

numbers = ["+1-555-1234", "123-456-7890", "5551234"]
for number in numbers:
    validate_phone_number(number)
