from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self):
        wd = self.app.wd
        self.open_add_page()
        # create contact
        self.fill_contact(Contact(firstname="qaa", lastname="qaaa", company="qaqaaa", home="qwea",
        work="qwew", email="qweaw@qa.qa", bday="25", bmonth="December", byear="1999"))
        # submit create contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # click to home for verify creation
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modified_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        # select modified
        wd.find_element_by_name("modifiy").click()
        # input changes
        self.fill_contact(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
        work="qwe", email="qwe@qa.qa", bday="26", bmonth="December", byear="1997"))
        # update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def fill_contact(self, Contact):
        wd = self.app.wd
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