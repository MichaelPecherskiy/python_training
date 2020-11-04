from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, Contact):
        wd = self.app.wd
        self.open_add_page()
        # fill in firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        # fill in lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        # fill in compamy
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # fill in home
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home)
        # fill in work
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work)
        # fill in email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        # fill in b-day
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contact.bday)
        wd.find_element_by_xpath("//option[@value='26']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contact.bmonth)
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.byear)
        # submit create contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # click to home for verify creation
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")