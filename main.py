import os
import time

# constants
working_path = os.getcwd()
users_file = working_path + "/data/users.txt"
events_file = working_path + "/data/events.txt"
# categories for events
categories = ['Weddings', 'Concerts', 'Talent Shows', 'Seminars', 'Brand Activation']

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
Admin function

Contains:
    Event prompt
    Add event
    Modify Event

"""

def event_prompt(choice):
    # for event name, date, time, price, capacity and desc
    if not isinstance(choice, int):
        return choice

    # if choice is an integer, then return the corresponding event
    if choice == 1:
        return categories[0]
    elif choice == 2:
        return categories[1]
    elif choice == 3:
        return categories[2]
    elif choice == 4:
        return categories[3] 
    elif choice == 5:
        return categories[4]
def add_event():
    clear_screen()
    print("Add event.")
    print("Available categories: ")
    for element in categories:
        print(f"{categories.index(element) + 1}. {element}")
    try:
        event_category = event_prompt(int(input("Event Category: ")))
        event_name = event_prompt(input("Event name: "))
        event_date = event_prompt(input("Event date: "))
        event_time = event_prompt(input("Event time: "))
        event_venue = event_prompt(input("Event venue: "))
        event_price = event_prompt(input("Event price: "))
        event_capacity = event_prompt(input("Event capacity: "))
        event_description = event_prompt(input("Event description: "))
    except ValueError:
        print("Invalid input. Try again!")
        add_event()

    with open(events_file, "a") as file:
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        file.write(f"{line_count + 1} {event_category} {event_name} {event_date} {event_time} {event_venue} {event_price} {event_capacity} {event_description}\n")
    print("Event added.")
    time.sleep(1)
def modify_event():
    clear_screen()
    print("Modify event...")
def admin():

    print("Hi admin! Select options below: ")
    print("1. Create event.")
    print("2. Modify event record.")
    print("3. Display all records.")
    print("4. Search record of customer details.")
    print("5. Log out")

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
        elif choice == 5:
            print("Logging out...")
            clear_screen()
            return
    except ValueError:
        print("Error! Invalid value. Try again!")
        time.sleep(1)
        clear_screen()
        admin()
    main()

"""
Registered customer functions
"""

def customer():
    print("Welcome! Select options below: ")
    print("1. Event Details ")
    print("2. Checkout ")
    print("3. Exit ")

    def eventcategory():
        print("Event Category: ")
        print("1. ")
    
    def events():
        print("Events: ")
        print("1. ")
    
    def checkout():
        print("Checkout: ")
        print("1. ")

    try:
        options = int(input("Choice: "))
        if options == 1:
            eventcategory()
        elif options == 2:
            events()
        elif options == 3:
            checkout()
        elif options == 4:
            print("Exiting...")
            time.sleep(1)
            clear_screen()
            return
    except ValueError:
        print("Invalid choice.")
        time.sleep(1)
        customer()
    customer()

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
Unregistered user function
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
