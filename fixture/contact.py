from model.contact import Contact
import re


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
        self.type_contact("home", Contact.homephone)
        self.type_contact("work", Contact.workphone)
        self.type_contact("mobile", Contact.mobilephone)
        self.type_contact("phone2", Contact.secondaryphone)
        self.type_contact("email", Contact.email)
        self.type_contact("email2", Contact.email2)
        self.type_contact("email3", Contact.email3)
        self.type_contact("address", Contact.address)
        self.type_contact("address2", Contact.secundaryaddress)

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[2].text
                firstname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                all_address = cells[3].text
                self.contact_cash.append(Contact(firstname=firstname,
                                                 lastname=lastname,
                                                 id=id,
                                                 all_phones_from_home_page=all_phones,
                                                 all_emails_from_home_page=all_emails,
                                                 all_address_from_home_page=all_address))
            return list(self.contact_cash)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname,
                       lastname=lastname,
                       id=id,
                       homephone=homephone,
                       workphone=workphone,
                       mobilephone=mobilephone,
                       secondaryphone=secondaryphone,
                       email=email,
                       email2=email2,
                       email3=email3,
                       address=address)


    def contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone,
                       workphone=workphone,
                       mobilephone=mobilephone,
                       secondaryphone=secondaryphone)


