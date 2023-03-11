import random
def generate_code(lenght=8):
    numbers = 'abcdef0123456789'
    return ''.join(random.choice(numbers) for _ in range(lenght))


