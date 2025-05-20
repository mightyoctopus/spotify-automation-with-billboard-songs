import random
import string

def generate_random_string(num):
    return ''.join(random.choices(string.ascii_lowercase, k=num))


