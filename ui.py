# a separator to make things look nice
def separator():
    print(100*"-")

# welcoming the user and take his name
def welcome():
    print("Welcome to project Zero!")
    separator()
    user_name = input("What's your name?\n")
    separator()
    print(f"Hello, {user_name}! Let's see if software development is for you.")
    separator()
    return user_name

# all user info
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
   