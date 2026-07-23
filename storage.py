# importing and calling the functions from the other files
import json


# save the user info
def save_user_data(user):
    with open("user_data.json", "w") as f:
        json.dump(user, f, indent=4)
        
# load the exsting info
def load_user_data():
    try:
        with open("user_data.json", "r") as f:
            user = json.load(f)
            return user
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    