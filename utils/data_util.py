import time
import random

def generate_dynamic_email():
    """Generates a unique email based on current timestamp."""
    timestamp = int(time.time())
    return f"automationtestqa{timestamp}@yopmail.com"

def generate_indonesia_phone():
    """Generates a random Indonesian phone number (08 + 9 digits)."""
    random_digits = random.randint(100000000, 999999999)
    return f"08{random_digits}"