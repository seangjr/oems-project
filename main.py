import os
import time

# constants
working_path = os.getcwd()
users_file = working_path + "/data/users.txt"
events_file = working_path + "/data/events.txt"

# categories for events
categories = ['Weddings', 'Concerts',
              'Talent_Shows', 'Seminars', 'Brand_Activation']

# clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def event_prompt(choice):
    # for event name, date, time, price, capacity and desc
    # if not type int returns input
    if not isinstance(choice, int):
        return choice.replace(" ", "_")

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

def display_categories():
    # display categories for user to choose from
    print("Event Categories: ")
    for element in categories:
        print(f"{categories.index(element) + 1}. {element.replace('_', ' ')}")


def event_list():
    display_categories()
    category = event_prompt(int(input("Event Category: ")))
    with open(events_file, 'r') as file:
        for line in file:
            # if category matches, print event
            # split line by space
            event_details = line.split()
            event_index = event_details[0]
            event_category = event_details[1]
            event_name = event_details[2]
            event_date = event_details[3]
            event_time = event_details[4]
            event_venue = event_details[5]
            event_price = event_details[6]
            event_capacity = event_details[7]
            # display event details in category
            if event_category == category:
                print(f"{event_index} Category: {event_category}, Name: {event_name.replace('_', ' ')}, Date: {event_date}, Time: {event_time}, Venue: {event_venue.replace('_', ' ')}, Price: {event_price}, Capacity: {event_capacity}")


def admin(username):

    def add_event():
        clear_screen()
        print("Add event.")
        display_categories()
        try:
            # event number [0]
            with open(events_file, 'r') as file:
                event_number = 1
                for line in file.readlines():
                    event_number += line.count('\n')
            # index [1]
            event_category = event_prompt(int(input("Event Category: ")))
            # event name [2]
            event_name = event_prompt(input("Event name: "))
            # event date [3]
            event_date = event_prompt(input("Event date (dd-mm-yy): "))
            # event time [4]
            event_time = event_prompt(input("Event time (24 hour format): "))
            # event venue [5]
            event_venue = event_prompt(input("Event venue: "))
            # event price [6]
            event_price = event_prompt(input("Event price (RM): "))
            # event capacity [7]
            event_capacity = event_prompt(input("Event capacity: "))
        except ValueError:
            print("Invalid input. Try again!")
            add_event()
        # write to text file
        with open(events_file, "a") as file:
            file.write(
                f"{event_number} {event_category} {event_name} {event_date} {event_time} {event_venue} {event_price} {event_capacity}\n")
        print("Event added.")
        time.sleep(1)
        # recursive call
        admin(username)

    def modify_event():
        clear_screen()
        print("List of events... choose a category to display an event!")
        event_list()
        print("Modify event. Please enter the event number to modify: ")
        event_to_modify = int(input("Event number: "))
        with open(events_file, 'r') as file:
            # read file line by line -> output to list var filedata
            filedata = file.readlines()

        for line in filedata:
            # store line in a variable
            temp_line = line
            # if event number matches, modify event
            if line[:1] == str(event_to_modify):
                # split line by space
                event_details = line.split()
                event_index = event_details[0]
                event_category = event_details[1]
                event_name = event_details[2]
                event_date = event_details[3]
                event_time = event_details[4]
                event_venue = event_details[5]
                event_price = event_details[6]
                event_capacity = event_details[7]
                # display event details
                print(f"{event_index} Category: {event_category}, Name: {event_name.replace('_', ' ')}, Date: {event_date}, Time: {event_time}, Venue: {event_venue.replace('_', ' ')}, Price: {event_price}, Capacity: {event_capacity}")
                print("Please enter the field you want to modify: \n1. Category\n2. Name\n3. Date\n4. Time\n5. Venue\n6. Price\n7. Capacity")
                # get user input
                choice = int(input("Choice: "))
                # modify event based on user input
                if choice == 1:
                    display_categories()
                    line = line.replace(event_category, event_prompt(
                        int(input("New category: "))))
                elif choice == 2:
                    line = line.replace(
                        event_name, event_prompt(input("New name: ")))
                elif choice == 3:
                    line = line.replace(
                        event_date, event_prompt(input("New date: ")))
                elif choice == 4:
                    line = line.replace(
                        event_time, event_prompt(input("New time: ")))
                elif choice == 5:
                    line = line.replace(
                        event_venue, event_prompt(input("New venue: ")))
                elif choice == 6:
                    line = line.replace(
                        event_price, event_prompt(input("New price: ")))
                elif choice == 7:
                    line = line.replace(
                        event_capacity, event_prompt(input("New capacity: ")))

                # replace old line with new line, while preserving the rest of the file
                filedata = [item.replace(temp_line, line) for item in filedata]

        # write to file
        with open(events_file, 'w') as file:
            file.writelines(filedata)
        print("Event modified...")
        time.sleep(1)
        admin(username)

    def display_event():
        clear_screen()
        print(f"Displaying all events...")
        event_list()
        choice = input("Type 'e' to exit when ready: ")
        # exit if user types 'e'
        if choice.lower() != "e":
            print("Invalid input!")
            time.sleep(2)
            display_event()
        else:
            admin(username)

    def customer_details():
        def display_customer_registration():
            clear_screen()
            # display customer registration details 
            with open(users_file, 'r') as file:
                for line in file:
                    # split line by space
                    user_details = line.split()
                    user = user_details[0]
                    permission = user_details[2]
                    registration_date = user_details[3]
                    # display customer registration details
                    if permission != "True":
                        print(
                            f"Username: {user}, Registration Date: {registration_date}")

            # exit when 'e' is entered
            choice = input("Type 'e' to exit when ready: ")
            if choice.lower() != "e":
                print("Invalid input!")
                time.sleep(2)
                display_event()
            else:
                admin(username)

        def search_customer_registration():
            clear_screen()
            print("Search customer registration.")
            # search customer registration based on search query and returns result if username contains search query
            search_username = str(input("Search username: "))
            with open(users_file, 'r') as file:
                print(
                    f"Searching usernames starting with '{search_username}'...")
                # read file line by line
                for line in file:
                    # split line by space
                    user_details = line.split()
                    user = user_details[0]
                    permission = user_details[2]
                    registration_date = user_details[3]
                    # display customer registration details
                    if permission != "True":
                        # if username contains search query
                        print(f"Username: {user}\nRegistration Date: {registration_date}") if user.startswith(
                            search_username) else print("No results.")

            # exit when 'e' is entered
            choice = input("Type 'e' to exit when ready: ")
            if choice.lower() != "e":
                print("Invalid input!")
                time.sleep(2)
                search_customer_registration()
            else:
                admin(username)

        # customer details menu
        clear_screen()
        print("Customer details! Select an option below: \n1. Display customer registration\n2. Display customer payment\n3. Search customer registration\n4. Search customer payment\n5. Back")
        choice = int(input("Choice: "))
        if choice == 1:
            display_customer_registration()
        elif choice == 2:
            print("2")
        elif choice == 3:
            search_customer_registration()
        elif choice == 4:
            print("4")
        elif choice == 5:
            admin(username)

    # admin main menu
    clear_screen()
    print(f"Hi {username}! Select options below: ")
    print("1. Create event.")
    print("2. Modify event record.")
    print("3. Display all records.")
    print("4. More options for customer details.")
    print("5. Log out.")
    # try catch to handle invalid input
    try:
        choice = int(input("Choice: "))
        if choice == 1:
            add_event()
        elif choice == 2:
            modify_event()
        elif choice == 3:
            display_event()
        elif choice == 4:
            customer_details()
        elif choice == 5:
            print("Logging out...")
            clear_screen()
            return
    except ValueError:
        print("Error! Invalid value. Try again!")
        time.sleep(1)
        clear_screen()
        admin(username)
    main()


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
            checkout()
        elif options == 3:
            print("Exiting...")
            time.sleep(1)
            clear_screen()
            return
    except ValueError:
        print("Invalid choice.")
        time.sleep(1)
        customer()
    customer()


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
    # create user file
    user_permission = False
    # date registered for user
    date_registered = time.strftime("%d/%m/%Y")
    # write to text file
    with open(users_file, "a") as file:
        file.write(
            f"{username} {password} {user_permission} {date_registered}\n")
    print("Account created.")
    time.sleep(1)
    clear_screen()

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
                    admin(username)
                else:
                    customer()
                time.sleep(1)
                return

    print("Invalid username or password.")
    time.sleep(1)
    clear_screen()


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
