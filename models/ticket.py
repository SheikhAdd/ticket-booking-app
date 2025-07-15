import uuid

class Ticket:
    def __init__(self, user, row, seat):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.phone = user.phone
        self.row = row
        self.seat = seat
        self.guid = str(uuid.uuid4())

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "row": self.row,
            "seat": self.seat,
            "guid": self.guid
        }
