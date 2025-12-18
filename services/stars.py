import random

def generate_stars(count):
    stars = []
    for _ in range(count):
        stars.append({
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
            "size": random.randint(1, 3)
        })
    return stars




