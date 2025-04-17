import random

def fortune(filepath):
    with open(filepath, "r") as f:
        fortunes = f.read().split("%")
        fortune = random.choice(fortunes)
        print(fortune.strip())
        