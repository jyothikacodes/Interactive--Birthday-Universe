import random

def get_fortune(name):
    fortunes = [
        f"{name}, something beautiful is unfolding for you.",
        f"{name}, your patience will soon turn into power.",
        f"{name}, even the universe is rooting for you.",
        f"{name}, your story is just getting interesting.",
        f"{name}, greatness often begins quietly."
    ]
    return random.choice(fortunes)



