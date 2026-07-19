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
    user_name = input("What's your name?\n")
    separator()
    print(f"Hello, {user_name}! Let's see if software development is for you.")
    separator()
    return user_name

    
def ask_study_goals(study_goals=None):

    if study_goals is None:
        study_goals = []

    if len(study_goals) > 0:
        print(f"\nYou have entered {len(study_goals)} goal(s) so far.")
        print("Your current goals are:")
        for index, goal in enumerate(study_goals):
            print(f"{index+1}.{goal}")
        print("")

    print("What are your goals for this project? \nEnter '0' when you are done.")
    while True:
        goal = input(f"\nEnter the goal number {len(study_goals)+1}:\n")
        if goal == "0":
            break
        if goal in study_goals:
            print("You have already entered this goal. Please enter a different goal.")
            continue
        study_goals.append(goal)
    separator()
    return study_goals


def ask_excitement():
    while True:
        try:
            excited = int(input("Rate your excitement today:\n1.Extreme\n2.High\n3.Medioum\n4.Low\n5.Not excited\n"))

            if excited == 1:
                print("That's great! glad to see your excitement for this project!")
            elif excited == 2:
                print("That's decent! Keep up the motivation!")
            elif excited == 3:
                print("That's good! Keep up the motivation!")
            elif excited == 4:
                print("That's okay! Remember, every day is a new opportunity to learn and grow!")
            elif excited == 5:
                print("That's alright! Remember, it's okay to have off days. Keep pushing forward and you'll find your passion in software development!")
            else:
                print("Please enter a number between 1 and 5.")
                separator()
                continue
        except ValueError:
            print("Please enter a valid number.")
            separator()
            continue
        break
    separator()
    return excited


def ask_study_time():
    while True:
        try:
            study_time = input("How many hours do you plan to study today?\n")
            
            study_time = float(study_time)
            if study_time == 0:
                print("That's okay! Remember, it's important to take breaks and rest. You can always come back to studying later.")
            elif study_time > 0 and study_time <= 2:
                print(f"Hmmm! You plan to study for {study_time} hours today. Every step counts, so make sure to stay focused and motivated!")
            elif study_time > 2 and study_time <= 5:
                print(f"Awesome! You plan to study for {study_time} hours today. Make sure to pace yourself and take breaks when needed!")
            elif study_time > 5 and study_time <= 12:
                print(f"Impressive! You plan to study for {study_time} hours today. Remember to take care of yourself and get enough rest!")
            elif study_time > 12 and study_time <= 24:
                print(f"Wow! are You sure you want to study for {study_time} hours today? Make sure to take breaks and prioritize your health and well-being!")
                
            else:
                print("Please enter a number between 0 and 24.")
                separator()
                continue
        except ValueError:
            print("Please enter a valid number between 0 and 24.")
            separator()
            continue
        break
    separator()
    return study_time


def ask_prior_experience():    
    while True:
        experience = input("Do you have any prior experience in software development? (yes/no)\n")
    
        if experience.lower() == "yes":
            print("That's great! It looks like you have some background in software development.")
        elif experience.lower() == "no":
            print("That's okay! Everyone starts somewhere. I'm here to help you learn and grow.")
        else:
            print("Please enter 'yes' or 'no'.")
            separator()
            continue
        break
    separator()
    return experience


def user_summary(user):

    print("Here is a summary of your information:")
    for key, value in user.items():
        if key == "Study Goals":
            print(f"{key}:")
            for index, goal in enumerate(value):
                print(f"  {index+1}. {goal}")
        else:
            print(f"{key}: {value}")
    print("\nProject status: Active")
    separator()


def edit_user_info(user):
    while True:
        choice = input("What would you like to edit?\n1. Name\n2. Study Goals\n3. Excitement Level\n4. Planned Study Time\n5. Prior Experience\n6. Exit edit mode\n")
        if choice == "1":
            separator()
            user_name = input("Enter your new name:\n")
            user["Name"] = user_name
        elif choice == "2":
            separator()
            print("Editing Study Goals:")
            study_goals = ask_study_goals(user["Study Goals"])
            user["Study Goals"] = study_goals
        elif choice == "3":
            separator()
            excitement = ask_excitement()
            user["Excitement Level"] = excitement
        elif choice == "4":
            separator()
            study_time = ask_study_time()
            user["Planned Study Time"] = study_time
        elif choice == "5":
            separator()
            prior_experience = ask_prior_experience()
            user["Prior Experience"] = prior_experience
        elif choice == "6":
            separator()
            print("Exiting edit mode....")
            break
        else:
            print("Please enter a valid option.")
    separator()

if __name__ == "__main__":
    user_name = welcome()
    study_goals = ask_study_goals()
    print("Before we begin, let's check your excitement level for this project\n")
    excitement = ask_excitement()
    study_time = ask_study_time()
    print("Now, let's talk about your prior experience in software development\n")
    prior_experience = ask_prior_experience()


    user = {
        "Name": user_name,
        "Study Goals": study_goals,
        "Excitement Level": excitement,
        "Planned Study Time": study_time,
        "Prior Experience": prior_experience
    }
    

    while True:
        user_summary(user)
        edit = input("Would you like to edit your information or exit?\n1.Edit\n2.Exit\n")
        if edit == "1":
            edit_user_info(user)
            separator()
        elif edit == "2":
            print("Thank you for using Project Zero!")
            break
        else:
            print("Please enter '1' or '2'.")
            separator()
       