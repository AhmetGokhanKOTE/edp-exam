class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationRejectedEvent(Event):
    pass

class Applicant:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name):
        self.name = name

class CommunicationQueue:
    def __init__(self):
        self.queue = []

    def publish(self, event):
        self.queue.append(event)

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {event.__class__.__name__}, Payload: {event.payload}")

if __name__ == "__main__":
    applicant = Applicant("Gokhan KOTE")
    company = Company("Tec-9Team")
    queue = CommunicationQueue()

    queue.publish(ApplicationRejectedEvent({
        "applicant": applicant.name,
        "company": company.name,
        "reason": "Position Filled!!" }))

    queue.process_events()
