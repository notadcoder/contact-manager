class Contact:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        if self.email and self.phone:
            return "{} (email: {}, phone: {})".format(self.name, self.email, self.phone)
        elif self.email:
            return "{} (email: {})".format(self.name, self.email)
        elif self.phone:
            return "{} (phone: {})".format(self.name, self.phone)
        else:
            return self.name


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, index):
        self.contacts.pop(index)

    def modify_contact(self, index, new_name=None, new_email=None, new_phone=None):
        contact = self.contacts[index]
        if new_name:
            contact.name = new_name
        if new_email:
            contact.email = new_email
        if new_phone:
            contact.phone = new_phone

    def show_contacts(self):
        if not self.contacts:
            print("No contacts.")
        else:
            for i, contact in enumerate(self.contacts):
                print("Contact {}: {}".format(i+1, contact))


def main():
    contact_list = ContactList()

    while True:
        print()
        print("Choose an option:")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Modify contact")
        print("4. Show contacts")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            email = input("Enter email (optional): ")
            phone = input("Enter phone (optional): ")
            contact = Contact(name, email, phone)
            contact_list.add_contact(contact)
        elif choice == "2":
            index = int(input("Enter contact index to delete: "))
            contact_list.delete_contact(index-1)
        elif choice == "3":
            index = int(input("Enter contact index to modify: "))
            new_name = input("Enter new name (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            new_phone = input("Enter new phone (press enter to skip): ")
            contact_list.modify_contact(index-1, new_name, new_email, new_phone)
        elif choice == "4":
            contact_list.show_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
