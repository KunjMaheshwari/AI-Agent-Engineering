from datetime import datetime

def get_current_time():
    """Returns the current date and time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice():
    """Simulates rolling a six-sided die and returns the result."""
    import random
    return random.randint(1, 6)

def generate_password(length=12):
    """Generates a random password of the specified length."""
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))