from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_page()
        # create contact
        self.fill_contact(contact)
        # submit create contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # click to home for verify creation
        wd.find_element_by_link_text("home").click()
        self.open_add_page()
        self.contact_cash = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_add_page()
        self.contact_cash = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_first_modify(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def modified_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_modify()
        # select modified
        wd.find_element_by_name("modifiy").click()
        # input changes
        self.fill_contact(contact)
        # update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_add_page()
        self.contact_cash = None

    def select_modify_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        self.open_home_page()
        self.select_modify_by_index(index)
        # select button modify
        wd.find_element_by_name("modifiy").click()
        # open modification form
        self.fill_contact(new_contact_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_add_page()
        self.contact_cash = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def fill_contact(self, Contact):
        wd = self.app.wd
        self.type_contact("firstname", Contact.firstname)
        self.type_contact("lastname", Contact.lastname)
        self.type_contact("company", Contact.company)
        self.type_contact("home", Contact.home)
        self.type_contact("work", Contact.work)
        self.type_contact("email", Contact.email)

    def type_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cash = []
            for element in wd.find_elements_by_name("entry"):
                firstname = element.find_elements_by_tag_name("td")
                text = firstname[2].text
                text2 = firstname[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cash.append(Contact(firstname=text, lastname=text2, id=id))
            return list(self.contact_cash)