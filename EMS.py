import getpass

# Data storage
users = {"admin": "admin123"}  # username: password
events = {}  # event_id: event_details
event_registrations = {}  # event_id: [list_of_registered_users]
feedbacks = {}  # event_id: [feedbacks]

# Main Menu
def main():
    while True:
        print("\n=== Event Management System ===")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Register as User")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            admin_login()
        elif choice == "2":
            user_login()
        elif choice == "3":
            register_user()
        elif choice == "4":
            print("Thank you for using the Event Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Admin Functions
def admin_login():
    username = input("Enter admin username: ")
    password = getpass.getpass("Enter admin password: ")
    if users.get(username) == password and username == "admin":
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid admin credentials.")

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Create Event")
        print("2. View Events")
        print("3. View Registrations")
        print("4. View Feedback")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            view_registrations()
        elif choice == "4":
            view_feedback()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def create_event():
    print("\n=== Create Event ===")
    event_id = input("Enter Event ID: ")
    if event_id in events:
        print("Event ID already exists. Please try again.")
        return
    event_name = input("Enter Event Name: ")
    event_date = input("Enter Event Date (YYYY-MM-DD): ")
    event_venue = input("Enter Event Venue: ")
    max_participants = int(input("Enter Max Participants: "))
    events[event_id] = {
        "name": event_name,
        "date": event_date,
        "venue": event_venue,
        "max_participants": max_participants,
    }
    event_registrations[event_id] = []
    feedbacks[event_id] = []
    print(f"Event '{event_name}' created successfully!")

def view_events():
    print("\n=== View Events ===")
    if not events:
        print("No events available.")
        return
    for event_id, details in events.items():
        print(f"ID: {event_id}, Name: {details['name']}, Date: {details['date']}, Venue: {details['venue']}, Max Participants: {details['max_participants']}")

def view_registrations():
    print("\n=== View Registrations ===")
    if not event_registrations:
        print("No registrations available.")
        return
    for event_id, registered_users in event_registrations.items():
        print(f"Event ID: {event_id}, Registered Users: {', '.join(registered_users) if registered_users else 'None'}")

def view_feedback():
    print("\n=== View Feedback ===")
    if not feedbacks:
        print("No feedback available.")
        return
    for event_id, feedback_list in feedbacks.items():
        print(f"\nFeedback for Event '{events[event_id]['name']}':")
        for fb in feedback_list:
            print(f" - {fb}")
    
def edit_event(events):
    event_name = input("Enter the name of the event to edit: ")
    if event_name in events:
        print("What would you like to update?")
        print("1. Event Date")
        print("2. Venue")
        print("3. Maximum Participants")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_date = input("Enter the new date (DD-MM-YYYY): ")
            events[event_name]["date"] = new_date
        elif choice == "2":
            new_venue = input("Enter the new venue: ")
            events[event_name]["venue"] = new_venue
        elif choice == "3":
            new_max_participants = int(input("Enter the new maximum participants: "))
            events[event_name]["max_participants"] = new_max_participants
        else:
            print("Invalid choice.")
        print(f"Updated event details: {events[event_name]}")
    else:
        print("Event not found.")

def delete_event(events):
    event_name = input("Enter the name of the event to delete: ")
    if event_name in events:
        del events[event_name]
        print(f"Event '{event_name}' has been deleted.")
    else:
        print("Event not found.")

def recommend_events(events, registrations, user_name):
    print("Recommended Events for You:")
    registered_events = registrations.get(user_name, [])
    for event_name, details in events.items():
        if event_name not in registered_events:
            print(f"- {event_name}: {details}")


# User Functions
def register_user():
    print("\n=== Register as User ===")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please try another.")
        return
    password = getpass.getpass("Enter password: ")
    users[username] = password
    print("User registration successful!")

def user_login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if users.get(username) == password and username != "admin":
        print("User login successful!")
        user_menu(username)
    else:
        print("Invalid user credentials.")

def user_menu(username):
    while True:
        print("\n=== User Menu ===")
        print("1. View Events")
        print("2. Register for Event")
        print("3. Provide Feedback")
        print("4. View My Registered Events")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_events()
        elif choice == "2":
            register_for_event(username)
        elif choice == "3":
            provide_feedback(username)
        elif choice == "4":
            view_my_registered_events(username)
        elif choice == "5":
            print("User logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def register_for_event(username):
    print("\n=== Register for Event ===")
    view_events()
    event_id = input("Enter the Event ID to register: ")
    if event_id not in events:
        print("Invalid Event ID.")
        return
    if username in event_registrations[event_id]:
        print("You are already registered for this event.")
        return
    if len(event_registrations[event_id]) >= events[event_id]["max_participants"]:
        print("Event is full. Registration closed.")
        return
    event_registrations[event_id].append(username)
    print(f"Successfully registered for '{events[event_id]['name']}'.")

def provide_feedback(username):
    print("\n=== Provide Feedback ===")
    view_my_registered_events(username)
    event_id = input("Enter the Event ID to provide feedback: ")
    if event_id not in event_registrations or username not in event_registrations[event_id]:
        print("You are not registered for this event.")
        return
    feedback = input("Enter your feedback: ")
    feedbacks[event_id].append(feedback)
    print("Feedback submitted successfully!")

def view_my_registered_events(username):
    print("\n=== My Registered Events ===")
    user_events = [
        event_id for event_id, registered_users in event_registrations.items() if username in registered_users
    ]
    if not user_events:
        print("You are not registered for any events.")
        return
    for event_id in user_events:
        print(f"ID: {event_id}, Name: {events[event_id]['name']}")

def cancel_registration(users, registrations):
    user_name = input("Enter your username: ")
    if user_name in registrations:
        print("Your registered events:")
        for event in registrations[user_name]:
            print(f"- {event}")
        event_name = input("Enter the name of the event to cancel registration: ")
        if event_name in registrations[user_name]:
            registrations[user_name].remove(event_name)
            print(f"You have successfully canceled your registration for '{event_name}'.")
        else:
            print("You are not registered for this event.")
    else:
        print("You have no registrations.")

def send_notifications(events, registrations):
    print("Upcoming Event Notifications:")
    for event_name, event_details in events.items():
        print(f"Event: {event_name}")
        print(f"  Date: {event_details['date']}")
        print(f"  Venue: {event_details['venue']}")
        print("-" * 20)

def search_events(events):
    keyword = input("Enter a keyword to search for events (name, date, or venue): ").lower()
    print("Search Results:")
    for event_name, event_details in events.items():
        if (keyword in event_name.lower() or
                keyword in event_details["date"].lower() or
                keyword in event_details["venue"].lower()):
            print(f"- {event_name}: {event_details}")

def rate_event(ratings):
    event_name = input("Enter the name of the event you want to rate: ")
    if event_name in ratings:
        rating = int(input("Rate the event on a scale of 1 to 5: "))
        if 1 <= rating <= 5:
            ratings[event_name].append(rating)
            print("Thank you for your feedback!")
        else:
            print("Invalid rating. Please enter a value between 1 and 5.")
    else:
        print("Event not found.")

def edit_profile(users):
    username = input("Enter your username: ")
    if username in users:
        print("What would you like to update?")
        print("1. Name")
        print("2. Contact Info")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_name = input("Enter your new name: ")
            users[username]["name"] = new_name
        elif choice == "2":
            new_contact = input("Enter your new contact info: ")
            users[username]["contact"] = new_contact
        else:
            print("Invalid choice.")
        print(f"Updated profile: {users[username]}")
    else:
        print("User not found.")


# Run the program
main()
