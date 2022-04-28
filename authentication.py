import time
import os

from admin_func import admin

# clear screen function 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def permission():
    try:
        permission_prompt = str(input("Are you an admin? (y/n): "))
        if permission_prompt == "y" or permission_prompt == "Y":
            return True
        elif permission_prompt == "n" or permission_prompt == "N":
            return False
    except ValueError:
        print("Invalid choice.")
        time.sleep(1)
        clear_screen()
        permission()

def sign_up(dir: str):
    print("Sign up for an account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    confirm_password = str(input("Confirm password: "))
    # password confirmation
    if confirm_password != password:
        print("Passwords do not match.")
        time.sleep(1)
        clear_screen()
        return
    # check if username is taken
    with open(dir, "r") as file:
        for line in file:
            if line.split()[0] == username:
                print("Username taken.")
                time.sleep(1)
                return
    # admin permission
    user_permission = permission()
    # date registered for user
    date_registered = time.strftime("%d/%m/%Y")
    # write to text file
    with open(dir, "a") as file:
        file.write(f"{username} {password} {user_permission} {date_registered}\n")
    print("Account created.")
    time.sleep(1)
    clear_screen()

def log_in(dir: str, events_file: str):
    print("Log in to your account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    with open(dir, "r") as file:
        for line in file:
            """
            Read for username and password. 
            If username and password match, then authenticated.
            """
            if line.split()[0] == username and line.split()[1] == password:
                print("Logged in.")
                # call auth function
                if line.split()[2] == "True":
                    admin(events_file)
                else:
                    print("User")
                time.sleep(1)
                return
    print("Invalid username or password.")
    time.sleep(1)
    clear_screen()