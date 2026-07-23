# ==================================
# Project Zero 
# My goal is to discover whether software development truly fits me.
# ==================================

# importing and calling the functions from the other files
import json
from storage import save_user_data, load_user_data
from ui import separator, welcome, user_summary
from user import ask_study_goals, ask_excitement, ask_study_time, ask_prior_experience, edit_user_info, create_new_profile


# main function to run the program
if __name__ == "__main__":
    user = load_user_data() # load old data if there is any
    if user is not None:
        while True:
            print(f"Welcome back, {user['Name']}!")
            separator()
            choice = input("Would you like to:\n1. Continue\n2. Create new profile\n3. Exit\n").strip()
            if choice == "1":
                print("Continuing with your existing profile...")
                separator()
                break
            elif choice == "2":
                print("Creating a new profile...")
                separator()
                user = create_new_profile()
                break
            elif choice == "3":
                print("Thank you for using Project Zero!")
                exit()
            else:
                print("Please enter '1', '2', or '3'.")
                separator()
                continue
    else:
        user = create_new_profile() # create new profile if there is no data

    # this will show after the first register
    while True:
        user_summary(user)
        edit = input("Would you like to edit your information or exit?\n1.Edit\n2.Exit\n").strip()
        if edit == "1":
            edit_user_info(user)
            separator()
        elif edit == "2":
            print("Thank you for using Project Zero!")
            break
        else:
            print("Please enter '1' or '2'.")
            separator()
       