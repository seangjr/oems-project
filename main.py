import os
import time
from authentication import log_in, sign_up
# constants
working_path = os.getcwd()
users_file = working_path + "/data/users.txt"
events_file = working_path + "/data/events.txt"

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


# main function
def main():
    print("Welcome to Asian Event Management Services! Select options below: ")
    print("1. Sign up.")
    print("2. Log in.")
    print("3. Exit.")
    try:
        choice = int(input("Choice: "))
        if choice == 1:
            sign_up(users_file)
        elif choice == 2:
            log_in(users_file, events_file)
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
