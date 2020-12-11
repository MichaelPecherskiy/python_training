from sys import maxsize


class Contact:

    def __init__(self, firstname=None,
                 lastname=None,
                 company=None,
                 email=None,
                 id=None,
                 homephone=None,
                 workphone=None,
                 mobilephone=None,
                 secondaryphone=None,
                 address=None,
                 email2=None,
                 email3=None,
                 middlename=None,
                 nickname=None,
                 title=None,
                 fax=None,
                 homepage=None,
                 address2=None,
                 notes=None,
                 all_phones_from_home_page=None,
                 all_emails_from_home_page=None,
                 all_address_from_home_page=None):
        self.middlename = middlename
        self.notes = notes
        self.address2 = address2
        self.homepage = homepage
        self.fax = fax
        self.title = title
        self.nickname = nickname
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.email = email
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.address = address
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_address_from_home_page = all_address_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
