from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, home_phone=None, work_phone = None,
                 mobile_phone = None, secondary_phone = None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.secondary_phone = secondary_phone
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.lastname}:{self.firstname}:{self.home_phone}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and (
            self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize