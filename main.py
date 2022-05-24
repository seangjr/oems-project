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
    found = False
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
                found = True
                print(
                    f"Event no. {event_index} → Category: {event_category}, Name: {event_name.replace('_', ' ')}, Date: {event_date}, Time: {event_time}, Venue: {event_venue.replace('_', ' ')}, Price (RM): {event_price}, Capacity: {event_capacity}"
                )
    return found


def count_line(file: str):
    with open(file, 'r') as file:
        line_number = 1
        for line in file.readlines():
            line_number += line.count('\n')
    return line_number


def admin(username: str):

    def add_event():
        clear_screen()
        print("Add event.")
        display_categories()
        try:
            # event number [0]
            event_number = count_line(events_file)
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
        # recursive call
        return admin(username)

    def modify_event():
        clear_screen()
        print("List of events... choose a category to display an event!")
        event_found = event_list()
        with open(events_file, 'r') as file:
            # read file line by line -> output to list var filedata
            filedata = file.readlines()

        # loop through list and replace line
        for line in filedata:
            # store unmodified line in a variable, which will be used later
            temp_line = line
            # if event number matches, modify event
            if event_found:
                print("Modify event. Please enter the event number to modify: ")
                event_to_modify = int(input("Event number: "))

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
                    print(f"Event no. {event_index} → Category: {event_category}, Name: {event_name.replace('_', ' ')}, Date: {event_date}, Time: {event_time}, Venue: {event_venue.replace('_', ' ')}, Price: {event_price}, Capacity: {event_capacity}")
                    print("Please enter the field you want to modify: \n1. Category\n2. Name\n3. Date\n4. Time\n5. Venue\n6. Price\n7. Capacity\n8. Delete line\n9. Back")
                    # get user input
                    choice = int(input("Choice: "))
                    # modify event based on user input
                    if choice == 1:
                        display_categories()
                        line = line.replace(event_category, event_prompt(
                            int(input("Event Category: "))))
                    elif choice == 2:
                        line = line.replace(
                            event_name, event_prompt(input("Event name: ")))
                    elif choice == 3:
                        line = line.replace(event_date, event_prompt(
                            input("Event date (dd-mm-yy): ")))
                    elif choice == 4:
                        line = line.replace(event_time, event_prompt(
                            input("Event time (24 hour format): ")))
                    elif choice == 5:
                        line = line.replace(
                            event_venue, event_prompt(input("Event venue: ")))
                    elif choice == 6:
                        line = line.replace(event_price, event_prompt(
                            input("Event price (RM): ")))
                    elif choice == 7:
                        line = line.replace(event_capacity, event_prompt(
                            input("Event capacity: ")))
                    elif choice == 8:
                        # delete line
                        line = ""
                    elif choice == 9:
                        return admin(username)

                    # add error handling **
                    if choice not in range(1, 9):
                        print("Invalid input. Try again!")
                        return admin(username)

                    # replace old line with new line, while preserving the rest of the file
                    filedata = [item.replace(temp_line, line)
                                for item in filedata if item]

                    # filedata still contains empty strings, so remove them
                    modified_filedata = []
                    for strings in filedata:
                        if strings != "":
                            modified_filedata.append(strings)

                    # replace line number with new line number
                    modified_filedata = [item.replace(
                        item[:1], str(modified_filedata.index(item)+1)) for item in modified_filedata]

                    # write modified file data to file
                    with open(events_file, 'w') as file:
                        file.writelines(modified_filedata)

                    print("Event modified...")
                    return admin(username)
        print("No event found!")

    def display_event():
        clear_screen()
        print("Displaying all events...")
        event_found = event_list()
        print("No event found in this category!") if not event_found else ""
        choice = input("Type 'e' to exit when ready: ")
        # exit if user types 'e'
        if choice.lower() != "e":
            print("Invalid input!")
            time.sleep(2)
            return display_event()
        else:
            return admin(username)

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
                return display_customer_registration()
            else:
                return admin(username)

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
        print("Customer details! Select an option below: \n1. Display all customer registration\n2. Display customer payment\n3. Search customer registration\n4. Search customer payment\n5. Back")
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
    print(f"Hi {username}! Welcome to the admin panel! Select options below: ")
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
    return admin(username)


def view_events():
    # unregistered users view events
    clear_screen()
    print("Welcome! Select your options below!\n1. View all events by category\n2. Back")
    choice = int(input("Choice: "))
    if choice != 1 and choice != 2:
        print("Invalid input!")
        return
    if choice == 2:
        return
    clear_screen()
    event_found = event_list()
    if not event_found:
        print("No events found!")
    time.sleep(1)


def customer(username):
    clear_screen()
    print(f"Welcome {username}! Select options below: ")
    print("1. View event details.")
    print("2. Add events to cart.")
    print("3. Checkout.")
    print("4. Exit.")

    def selection():
        clear_screen()
        print("1. Event categories")
        print("2. Event details")

        selection_choice = int(input("Select an option to view details: "))
        if selection_choice == 1:
            # description of categories
            print("Weddings - ")
            print("Concerts - ")
            print("Talent Shows - ")
            print("Seminars - ")
            print("Brand Activation - ")
        elif selection_choice == 2:
            # details of events
            # if event not found in category, display message
            event_found = event_list()
            print("No event found in this category!") if not event_found else ""

            choice = input("Type 'e' to exit when done: ")
            if choice.lower() != "e":
                print("Invalid input!")
                time.sleep(2)
                return selection()
            else:
                return customer(username)

    # allow cart to accept multiple events
    def cart():
        # initialise list for cart
        cart = []
        # list for price of events in cart -> to be calculated for total price
        price_list = []

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

                print(f"Event no. {event_index} → Category: {event_category}, Name: {event_name.replace('_', ' ')}, Date: {event_date}, Time: {event_time}, Venue: {event_venue.replace('_', ' ')}, Price: {event_price}, Capacity: {event_capacity}")

            # if exited is True, then stop the loop
            exited = False
            while exited == False:
                cart_prompt = input(
                    "Enter an event number to add to cart or type 'e' to exit: ")

                if cart_prompt.lowercase() == 'e':
                    exited = True
                    break

                # if event number is valid, add to cart

        clear_screen()

    def checkout():
        print("1. E-wallet")
        print("2. Bank transfer")
        payment = int(input("Please select checkout method: "))

    try:
        options = int(input("Choice: "))
        if options == 1:
            selection()
        elif options == 2:
            cart()
        elif options == 3:
            checkout()
        elif options == 4:
            print("Exiting...")
            clear_screen()
            return
    except ValueError:
        print("Invalid choice.")
        return customer(username)
    return customer(username)


def sign_up():
    print("Sign up for an account.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    confirm_password = str(input("Confirm password: "))

    # check if password is more than 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters.")
        sign_up()

    # check if password and confirm password are the same
    if confirm_password != password:
        print("Passwords do not match.")
        return

    # check if username is taken
    with open(users_file, "r") as file:
        for line in file:
            user_details = line.split()
            if user_details[0] == username:
                print("Username taken.")
                return sign_up()

    # create user file. DEFAULTS TO FALSE -> customer permission
    user_permission = False
    # date registered for user
    date_registered = time.strftime("%d/%m/%Y")
    # write to text file
    with open(users_file, "a") as file:
        file.write(
            f"{username} {password} {user_permission} {date_registered}\n")
    print("Account created.")
    clear_screen()
    return main()


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
            user_details = line.split()
            if user_details[0] == username and user_details[1] == password:
                print("Logged in.")
                # call auth function
                if user_details[2] == "True":
                    # if user is admin
                    admin(username)
                else:
                    # else if user is customer call the customer function
                    customer(username)
                return

    print("Invalid username or password.")
    clear_screen()
    return main()

# main function


def main():
    print("Welcome to Asian Event Management Services! Select options below: ")
    print("1. Sign up.")
    print("2. Log in.")
    print("3. View events")
    print("4. Exit.")
    try:
        choice = int(input("Choice: "))
        if choice == 1:
            sign_up()
        elif choice == 2:
            log_in()
        elif choice == 3:
            view_events()
        elif choice == 4:
            print("Exiting...")
            clear_screen()
            exit()
    except ValueError:
        print("Invalid choice.")
        clear_screen()
        return main()
    main()


main()
