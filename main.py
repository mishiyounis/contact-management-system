import json
import os
from functions import *

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_contacts(contacts):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(f" Error saving: {e}")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n" + "="*50)
        print("     ADVANCED CONTACT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Filter Contacts (City/Company)")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Sort Contacts (A-Z)")
        print("8. Export to CSV")
        print("9. Import from CSV")
        print("10. Favorites")
        print("11. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-11): ")
        
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
            contacts = sort_contacts(contacts)
            save_contacts(contacts)
        elif choice == "8":
            export_to_csv(contacts)
        elif choice == "9":
            import_and_merge(contacts)
            save_contacts(contacts)
        elif choice == "10":
            favorites_menu(contacts)
            save_contacts(contacts)
        elif choice == "11":
            print("\nGoodbye!")
            break
        else:
            print(" Invalid choice. Enter 1-11.")

if __name__ == "__main__":
    main()