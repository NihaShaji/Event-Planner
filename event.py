class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.attendees = []

    def add_attendee(self, attendee_name):
        self.attendees.append(attendee_name)

class EventPlanner:
    def __init__(self):
        self.events = []

    def schedule_event(self):
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        location = input("Enter event location: ")
        new_event = Event(name, date, location)
        self.events.append(new_event)
        print(f"Event '{name}' has been scheduled successfully.")

    def reschedule_event(self):
        if not self.events:
            print("No events available to reschedule.")
            return

        self.view_events()
        event_index = int(input("Select the event to reschedule (Enter the number): ")) - 1
        if 0 <= event_index < len(self.events):
            event = self.events[event_index]
            new_date = input(f"Enter the new date for '{event.name}' (YYYY-MM-DD): ")
            new_location = input(f"Enter the new location for '{event.name}': ")
            
            event.date = new_date
            event.location = new_location
            print(f"Event '{event.name}' has been rescheduled to {new_date} at {new_location}.")
        else:
            print("Invalid event selection.")


    def send_invitation(self):
        if not self.events:
            print("No events available to send invitations.")
            return

        self.view_events()
        event_index = int(input("Select the event to send invitations (Enter the number): ")) - 1
        if 0 <= event_index < len(self.events):
            event = self.events[event_index]
            try:
                num_attendees = int(input("How many attendees would you like to add? "))
                for i in range(num_attendees):
                    attendee_name = input(f"Enter name of attendee {i+1}: ")
                    event.add_attendee(attendee_name)
                print(f"{num_attendees} attendees have been added to the event '{event.name}'.")
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
        else:
            print("Invalid event selection.")


    def view_events(self):
        if not self.events:
            print("No events scheduled yet.")
        else:
            print("\nUpcoming Events:")
            for i, event in enumerate(self.events, 1):
                print(f"{i}. {event.name} on {event.date} at {event.location}")
                if event.attendees:
                    print("   Attendees:")
                    for attendee in event.attendees:
                        print(f"     - {attendee}")
                else:
                    print("   No attendees have been added yet.")


    def filter_events_by_date(self):
        if not self.events:
            print("No events scheduled yet.")
            return

        date = input("Enter the date to filter events (YYYY-MM-DD): ")
        filtered_events = [event for event in self.events if event.date == date]

        if filtered_events:
            print(f"\nEvents on {date}:")
            for event in filtered_events:
                print(f"- {event.name} at {event.location}")
                if event.attendees:
                    print("   Attendees:")
                    for attendee in event.attendees:
                        print(f"     - {attendee}")
                else:
                    print("   No attendees have been added yet.")
        else:
            print(f"No events found on {date}.")


    def manage_event_planner(self):
        while True:
            print("\nEvent Planner Menu:")
            print("1. Schedule a new event")
            print("2. Reschedule an event")
            print("3. Send invitations (Add attendees)")
            print("4. View all events")
            print("5. Filter events by date")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.schedule_event()
            elif choice == "2":
                self.reschedule_event()
            elif choice == "3":
                self.send_invitation()
            elif choice == "4":
                self.view_events()
            elif choice == "5":
                self.filter_events_by_date()
            elif choice == "6":
                print("Thank you for using the Event Planner!")
                break
            else:
                print("Invalid choice. Please try again.")


planner = EventPlanner()
planner.manage_event_planner()
