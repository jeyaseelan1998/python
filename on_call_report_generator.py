class Event:
    """Event class used for events"""

    def __init__(self, date, user, machine, type) -> None:
        self.date = date
        self.user = user
        self.machine = machine
        self.type = type


def get_datetime(event):
    """This function returns date from event object"""
    return event.date


def get_users_status(events):
    """This function return user's status data dictionary"""
    users = {}
    events.sort(key=get_datetime)
    for event in events:
        if event.machine not in users:
            users[event.machine] = set()
        if event.type == "logged-in":
            users[event.machine].add(event.user)
        elif event.type == "logged-out" and event.user in users[event.machine]:
            users[event.machine].remove(event.user)
    return users


def generate_report(status):
    """This function generates report"""
    print()
    for server, users in status.items():
        print("{}:\n {}".format(server, ", ".join(users)))
    print()


# list of events
events = [
    Event("2023-01-24 10:54:41.602207", "jeyaseelan", "webserver", "logged-in"),
    Event("2023-01-23 10:54:41.602207", "guru", "localserver", "logged-out"),
    Event("2023-01-23 01:54:41.602207", "sandy", "localserver", "logged-in"),
    Event("2023-01-21 10:54:41.602207", "tamil", "webserver", "logged-in"),
    Event("2023-01-24 07:54:41.602207", "prakash", "localserver", "logged-in"),
    Event("2023-01-24 08:54:41.602207", "dhoni", "webserver", "logged-in")
]

status = get_users_status(events)

generate_report(status)
