import random
import string

def generate_password(length=12, complexity='medium'):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    if complexity == 'low':
        choices = lowercase_letters + numbers
    elif complexity == 'medium':
        choices = lowercase_letters + uppercase_letters + numbers
    elif complexity == 'high':
        choices = lowercase_letters + uppercase_letters + numbers + special_chars
    else:
        raise ValueError("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")

    password = ''.join(random.choices(choices, k=length))

    return password