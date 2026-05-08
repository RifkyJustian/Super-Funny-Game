import random
from config import MIN_NUMBER, MAX_NUMBER

def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)
