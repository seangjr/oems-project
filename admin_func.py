import time
import os

from categories import categories

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    else:
        return False

def add_event(events_file: str):
    clear_screen()
    print("Add event.")
    print("Available categories: ")
    for element in categories:
        print(f"{categories.index(element) + 1}. {element}")
    try:
        event_category = event_prompt(int(input("Event Category: ")))
        if event_category == False:
            print("Invalid choice.")
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
        add_event(events_file)

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

def admin(events_file: str):
    # main admin prompt
    print("Hi admin! Select options below: ")
    print("1. Create event.")
    print("2. Modify event record.")
    print("3. Display all records.")
    print("4. Search record of customer details.")
    print("5. Log out")

    try:
        choice = int(input("Choice: "))
        # create event
        if choice == 1:
            add_event(events_file)
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
        admin(events_file)

