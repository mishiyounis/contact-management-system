import json
import os
from functions import *

DATA_FILE = "contacts.json" # name of the file where the contacts will be stored.

def load_contacts():    # this is the function for loading contacts from the file.
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
        
    return[]

def save_contacts(contacts):     # this is the function for saving the contacts in the file.
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# MAIN MENU FUNCTION....

def main():
    contacts = load_contacts()  # for loading existing contact.

    while True:    # loop.
        print("\n" + "^"*50)
        print("         WELCOME TO CONTACT MANAGEMENT SYSTEM")
        print("^"*50)
        print("1. Add Contact")
        print("2. View all Contacts")
        print("3. Search Contacts")
        print("4. Filter Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        print("-"*50)     

        choice = input("enter your choice (1 to 7): ")     
        if choice == "1":
            contacts = add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_contacts(contacts)
        elif choice == "5":
            contacts = update_contact(contacts)
            save_contacts(contacts)
        elif choice == "6":
             contacts = delete_contact(contacts)
             save_contacts(contacts)    
        elif choice == "7":
            print("\nGoodbye!")

            break
        else:
            print("invalid choice. please enter 1 to 7.")

if __name__ == "__main__":
    main()