import os
import time
import authentication, admin_func

# constants
working_path = os.getcwd()
users_file = working_path + "/data/users.txt"
events_file = working_path + "/data/events.txt"
# categories for events
categories = ['Weddings', 'Concerts', 'Talent Shows', 'Seminars', 'Brand Activation']

# clear screen function 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def admin():
    # main admin prompt
    print("Hi admin! Select options below: ")
    print("1. Create event.")
    print("2. Modify event record.")
    print("3. Display all records.")
    print("4. Search record of customer details.")
    print("5. Log out")

    try:
        choice = int(input("Choice: "))
        if choice == 1:
            admin_func.add_event(events_file)
        elif choice == 2:
            admin_func.modify_event()
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

# main function
def main():
    print("Welcome to Asian Event Management Services! Select options below: ")
    print("1. Sign up.")
    print("2. Log in.")
    print("3. Exit.")
    try:
        choice = int(input("Choice: "))
        if choice == 1:
            authentication.sign_up(users_file)
        elif choice == 2:
            authentication.log_in(users_file, admin(), customer())
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
