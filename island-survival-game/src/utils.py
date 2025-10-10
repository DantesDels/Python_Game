def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def validate_input(user_input, valid_options):
    return user_input in valid_options

def format_gauge(value, max_value):
    return f"{'█' * (max_value - value)//10}{' ' * (value//10)} {value}/{max_value}"