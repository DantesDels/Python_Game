import os

def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def validate_input(user_input, valid_options):
    return user_input in valid_options

def clear_screen():
    if os.name == 'nt':
        os.system('cls') # Windows
    else:
        os.system('clear') # Unix/Linux/MacOS