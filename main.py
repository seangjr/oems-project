import os
import time

# constants
working_path = os.getcwd()
users_file = working_path + "/data/users.txt"
events_file = working_path + "/data/events.txt"

# clear screen function 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# user permission function to be called in sign up function 
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

"""
User sign up function.
"""
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
    with open(users_file, "r") as file:
        for line in file:
            if line.split()[0] == username:
                print("Username taken.")
                time.sleep(1)
                return
    # admin permission
    user_permission = permission()
    """
    Write username, password, date registered, and admin permission to text file.
    """
    # date registered for user
    date_registered = time.strftime("%d/%m/%Y")
    # write to text file
    with open(users_file, "a") as file:
        file.write(f"{username} {password} {user_permission} {date_registered}\n")
    print("Account created.")
    time.sleep(1)
    clear_screen()

"""
User login function
"""
def log_in():
    print("Log in to your account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    with open(users_file, "r") as file:
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
    clear_screen()
"""
Admin function
"""
def admin():

    print("Hi admin! Select options below: ")
    print("1. Create event.")
    print("2. Modify event record.")
    print("3. Display all records.")
    print("4. Search record of customer details.")

    def add_event():
        clear_screen()
        print("Add event.")
        event_category = str(input("Event category: "))
        event_name = str(input("Event name: "))
        event_date = str(input("Event date: "))
        event_time = str(input("Event time: "))
        event_venue = str(input("Event venue: "))
        event_price = str(input("Event price: "))
        event_capacity = str(input("Event capacity: "))
        event_description = str(input("Event description: "))
        with open(events_file, "a") as file:
            line_count = 0
            for line in file:
                if line != "\n":
                    line_count += 1
            file.write(f"{line_count + 1} {event_category} {event_name} {event_date} {event_time} {event_venue} {event_price} {event_capacity} {event_description}\n")
        print("Event added.")
        time.sleep(1)
        clear_screen()
    
    def modify_event():
        clear_screen()
        print("Modify event...")
        # with open(events_file, 'r') as file:
        #     for line in file:
        #         event_information = line.split() 

    try:
        choice = int(input("Choice: "))
        if choice == 1:
            add_event()
        elif choice == 2:
            modify_event()
        elif choice == 3:
            print("3")
            # display_events()
        elif choice == 4:
            print("4")
            # search_customer()
    except ValueError:
        print("Invalid input!")
        time.sleep(1)
    time.sleep(1)
"""
Registered user function
"""
def user_menu():
    # user menu
    print("User menu.")

# main function
def main():
    print("Welcome to Asian Event Management Services! Select options below: ")
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
            clear_screen()
            exit()
    except ValueError:
        print("Invalid choice.")
        time.sleep(1)
        clear_screen()
        main()
    main()
    return 0

if __name__ == "__main__":
    main()