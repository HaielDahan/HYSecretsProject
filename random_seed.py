import random

def generate_random_list(number,size):
    random.seed(number)
    random_list = []
    total = 0
    while total < size:
        value = random.randint(1, 18)
        if total + value > size:
            break
        random_list.append(value)
        total += value
    return random_list


def get_random_seed():
    return random.randint(1, 256)