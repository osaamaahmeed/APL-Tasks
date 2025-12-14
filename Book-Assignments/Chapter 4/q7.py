import re

def replace_credit_card_numbers(text):
    pattern = r"\d(?=(?:\D*\d){4})"
    masked_text = re.sub(pattern, "*", text)
    return masked_text

text = "Card: 1234-4567-9012-3456"
print(replace_credit_card_numbers(text))