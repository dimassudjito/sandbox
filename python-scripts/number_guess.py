import random

print("Your kid just received his math score but he doesn't want to tell you the score")
print("You have to make a correct guess to find out")

answer = random.randint(0,101)
guess = int(input("Make a guess:"))

while guess != answer:
    if guess > answer:
        print("His score is not that big")
    else:
        print("His score is not that small")
    guess = int(input("Make another guess:"))

print("Yes his score is " + str(answer))




