import random

items = ["apple", "banana", "cherry", "orange", "grape"]

def pick_random():
    return random.choice(items)

if __name__ == "__main__":
    print("Random choice:", pick_random())
