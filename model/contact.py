from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, id=None,
                 all_phones_from_home_page=None,
                 home_phone=None, work_phone=None,
                 mobile_phone=None, secondary_phone=None,
                 email1=None, email2=None, email3=None, all_email=None,
                 address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_email = all_email
        self.address = address
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.lastname}:{self.firstname}:{self.nickname}:{self.home_phone}:" \
               f"{self.mobile_phone}:{self.work_phone}:{self.secondary_phone}:" \
               f"{self.email1}:{self.email2}:{self.email3}:{self.address}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and (
            self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize