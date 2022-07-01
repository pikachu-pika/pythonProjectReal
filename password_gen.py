import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
meta = string.punctuation
digits = string.digits

characters = f"{upper}{digits}{lower}{meta}"


def pass_gen(size):
    password = "".join([random.choice(characters) for _ in range(size)])
    return password



