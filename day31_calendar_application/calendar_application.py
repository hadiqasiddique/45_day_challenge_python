import datetime

class Event:
    def __init__(self, title, date, description=""):
        #Initialize an event with title, date, and optional description.
        self.title = title
        self.date = date
        self.description = description

    def __str__(self):
        #Return a nicely formatted string for the event.
        return f"Title: {self.title} | Date: {self.date.strftime('%Y-%m-%d')} | Description: {self.description}"


class Calendar:
    def __init__(self):
        #Initialize an empty calendar with a list of events.
        self.events = []

    def add_event(self, event):
        #Add an event to the calendar.
        self.events.append(event)
        print(f" Event '{event.title}' added to the calendar.")

    def view_events(self):
        #View all events in the calendar.
        if not self.events:
            print(" No events in the calendar.")
        else:
            print("\n Your Events:")
            for event in self.events:
                print(event)

    def delete_event(self, title):
        #Delete an event by its title.
        event_to_delete = None
        for event in self.events:
            if event.title.lower() == title.lower():
                event_to_delete = event
                break

        if event_to_delete:
            self.events.remove(event_to_delete)
            print(f"Event '{title}' deleted from the calendar.")
        else:
            print(" Event not found.")


def main():
    calendar = Calendar()

    while True:
        print("\n=== Calendar Menu ===")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter event title: ")
            date_input = input("Enter event date (YYYY-MM-DD): ")

            try:
                date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            description = input("Enter event description (optional): ")

            event = Event(title, date, description)
            calendar.add_event(event)

        elif choice == "2":
            calendar.view_events()

        elif choice == "3":
            title = input("Enter the title of the event to delete: ")
            calendar.delete_event(title)

        elif choice == "4":
            print("Exiting the calendar application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
