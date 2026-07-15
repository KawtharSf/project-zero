# ==================================
# Project Zero - Day 1
# My goal is to discover whether software development truly fits me.
# ==================================

print("Welcome to project Zero!")
print(100*"-")
name = input("What's your name?\n")
print(100*"-")

print(f"Hello, {name}! Let's see if software development is for you.")
print(100*"-")

goal = input("What is your goal for this project?\n")
print(100*"-")

print(f"Name: {name}\nGoal: {goal}\nProject status: Active")
print(100*"-")

while True:

    try:
        excited = int(input("Rate your excitement today on a scale of 1-10\n"))
        print(100*"-")
    except ValueError:
        print("Please enter a valid number between 1 and 10.")
        print(100*"-")
        continue

    if excited<1 or excited>10:
        print("Please enter a valid number between 1 and 10.")
        print(100*"-")
        continue
    else:
        break

if excited >= 8:
    print("That's great! glad to see your excitement for this project!")
elif excited >= 5:
    print("That's good! Keep up the motivation!")
else:
    print("That's okay! Remember, every day is a new opportunity to learn and grow!")


