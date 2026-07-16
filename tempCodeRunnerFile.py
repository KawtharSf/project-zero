# ==================================
# Project Zero - Day 1
# My goal is to discover whether software development truly fits me.
# ==================================

def separator():
    print(100*"-")
separator()

def welcome():
    print("Welcome to project Zero!")
    separator()

    name = input("What's your name?\n")
    separator()

    print(f"Hello, {name}! Let's see if software development is for you.")
    separator()

    goal = input("What is your goal for this project?\n")
    separator()

    print(f"Name: {name}\nGoal: {goal}\nProject status: Active")
    separator()

def excitement():
    print("Before we begin, let's check your excitement level for this project.")
    separator()
    while True:
        try:
            excited = int(input("Rate your excitement today:\n1.Extreme\n2.High\n3.Medioum\n4.Low\n5.Not excited\n"))
            separator()

            if excited == 1:
                print("That's great! glad to see your excitement for this project!")
                break
            elif excited == 2:
                print("That's decent! Keep up the motivation!")
                break
            elif excited == 3:
                print("That's good! Keep up the motivation!")
                break
            elif excited == 4:
                print("That's okay! Remember, every day is a new opportunity to learn and grow!")
                break
            elif excited == 5:
                print("That's alright! Remember, it's okay to have off days. Keep pushing forward and you'll find your passion in software development!")
                break
            else:
                print("Please enter a number between 1 and 5.")
                separator()
                continue
        except ValueError:
            print("Please enter a valid number.")
            separator()
            continue


def study_time():
    print("Now, let's talk about your study time for today.")
    separator()
    while True:
        try:
            study_time = input("\nHow many hours do you plan to study today?\n")
            separator()
            study_time = float(study_time)
            if study_time == 0:
                print("That's okay! Remember, it's important to take breaks and rest. You can always come back to studying later.")
                break
            elif study_time > 0 and study_time <= 2:
                print(f"Hmmm! You plan to study for {study_time} hours today. Every step counts, so make sure to stay focused and motivated!")
                break
            elif study_time > 2 and study_time <= 5:
                print(f"Awesome! You plan to study for {study_time} hours today. Make sure to pace yourself and take breaks when needed!")
                break
            elif study_time > 5 and study_time <= 12:
                print(f"Impressive! You plan to study for {study_time} hours today. Remember to take care of yourself and get enough rest!")
                break
            elif study_time > 12 and study_time <= 24:
                print(f"Wow! are You sure you want to study for {study_time} hours today? Make sure to take breaks and prioritize your health and well-being!")
                break
            else:
                print("Please enter a number between 0 and 24.")
                separator()
                continue
        except ValueError:
            print("Please enter a valid number between 0 and 24.")
            separator()
            continue

def prior_experience():
    print("Now, let's talk about your prior experience in software development.")
    separator()
    while True:
        experience = input("\nDo you have any prior experience in software development? (yes/no)\n")
        separator()
        if experience.lower() == "yes":
            print("That's great! It looks like you have some background in software development.")
            break
        elif experience.lower() == "no":
            print("That's okay! Everyone starts somewhere. I'm here to help you learn and grow.")
            break
        else:
            print("Please enter 'yes' or 'no'.")
            separator()
            continue

if __name__ == "__main__":
    welcome()
    excitement()
    study_time()
    prior_experience()
    print("Thank you for sharing your thoughts and goals with me. Let's make this project a success!")
    separator()