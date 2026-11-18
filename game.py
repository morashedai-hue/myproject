
import time
import random
import os

os.system("")

RED = "\033[91m"
PINK = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

name = input("اكتب الاسم اللي بتحبه: ")

os.system("cls")

hearts = ["❤️", "💖", "💕", "💗", "💘"]

print("\n")

for i in range(3):
    print(PINK + " " * 15 + random.choice(hearts) * 5 + RESET)
    time.sleep(0.5)

print("\n")

messages = [
    "Preparing something special...",
    "Collecting beautiful moments...",
    "Loading love...",
    "Almost ready..."
]

for message in messages:
    print(WHITE + message + RESET)
    time.sleep(1)

print("\n")

for i in range(3):
    print(RED + " " * 20 + "♥" + RESET)
    time.sleep(0.4)

os.system("cls")

print("\n")
print(PINK + " " * 10 + "♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥" + RESET)
print()

time.sleep(0.5)

print(RED + BOLD + " " * 12 + f"I LOVE YOU, {name.upper()}!" + RESET)

time.sleep(0.5)

print(PINK + " " * 10 + "♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥" + RESET)

print("\n")
print(WHITE + " " * 12 + "You are special ❤️" + RESET)
print("\n")

time.sleep(1)

print(PINK + " " * 15 + "FOREVER ❤️" + RESET)
