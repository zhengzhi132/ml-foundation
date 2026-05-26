class contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class ContactsManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone):
        new_contact = contact(name, phone)
        self.contacts.append(new_contact)
    
    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")
    
    def find_contact_with_name(self, name):
        for contact in self.contacts:
            if contact.name == name :
                return contact
        return None 
    
    def find_contact_with_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone :
                return contact
        return None
    
    def delete_contact(self, name):
        contact = self.find_contact_with_name(name)
        if contact:
            self.contacts.remove(contact)
        else:
            print(f"Contact with name {name} not found.")
manager = ContactsManager()
manager.add_contact("Alice", "123456789")
manager.add_contact("Bob", "987654321")
while True:
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Find Contact by Name")
    print("4. Find Contact by Phone")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        manager.add_contact(name, phone)
    elif choice == "2":
        manager.list_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        contact = manager.find_contact_with_name(name)
        if contact:
            print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("Contact not found.")
    elif choice == "4":
        phone = input("Enter phone to search: ")
        contact = manager.find_contact_with_phone(phone)
        if contact:
            print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("Contact not found.")
    elif choice == "5":
        name = input("Enter name to delete: ")
        manager.delete_contact(name)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
