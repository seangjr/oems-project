import os
import time
# constants
working_path = os.getcwd()
text_file = working_path + "/data/users.txt"

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

        permission()
        
def sign_up():
    print("Sign up for an account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    confirm_password = str(input("Confirm password: "))
    # password confirmation
    if confirm_password != password:
        print("Passwords do not match.")
        time.sleep(1)
        return
    # check if username is taken
    with open(text_file, "r") as file:
        for line in file:
            if line.split()[0] == username:
                print("Username taken.")
                time.sleep(1)
                return
    # admin permission
    user_permission = permission()
    # write to file
    with open(text_file, "a") as file:
        file.write(f"{username} {password} {user_permission}\n")
    print("Account created.")
    time.sleep(1)

def log_in():
    print("Log in to your account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    with open(text_file, "r") as file:
        for line in file:
            """
            Read for username and password. 
            If username and password match, then authenticated.
            """
            if line.split()[0] == username and line.split()[1] == password:
                print("Logged in.")
                # call auth function
                if line.split()[2] == "True":
                    admin()
                else:
                    user_menu()
                time.sleep(1)
                return
    print("Invalid username or password.")
    time.sleep(1)

def admin():
    # if users see this means they are logged in as admin
    print("Admin.")
    time.sleep(1)

def user_menu():
    # user menu
    print("User menu.")

def main():
    print("Welcome to the cool-stuff app.")
    print("1. Sign up.")
    print("2. Log in.")
    print("3. Exit.")
    try:
        choice = int(input("Choice: "))
        if choice == 1:
            sign_up()
        elif choice == 2:
            log_in()
        elif choice == 3:
            print("Exiting...")
            time.sleep(1)
            exit()
    except ValueError:
        print("Invalid choice.")
        time.sleep(1)
        main()
    main()
    return 0

main()