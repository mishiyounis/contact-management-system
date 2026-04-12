import re
import csv

# ========== VALIDATION FUNCTIONS ==========

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

def get_non_empty_input(prompt):
    """Strong input validation - no empty values allowed"""
    value = input(prompt).strip()
    while not value:
        print("  This field cannot be empty!")
        value = input(prompt).strip()
    return value

# ========== UNIQUE ID GENERATION ==========

def get_next_id(contacts):
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

# ========== ADD CONTACT ==========

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    
    name = get_non_empty_input("Full Name: ")
    
    while True:
        phone = get_non_empty_input("Phone Number: ")
        if is_valid_phone(phone):
            break
        print("  Invalid phone! Must be at least 10 digits, numbers only.")
    
    while True:
        email = get_non_empty_input("Email Address: ")
        if is_valid_email(email):
            break
        print("  Invalid email! Example: name@domain.com")
    
    city = get_non_empty_input("City: ")
    company = get_non_empty_input("Company: ")
    
    new_contact = {
        "id": get_next_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "company": company,
        "favorite": False
    }
    
    contacts.append(new_contact)
    print(f"\n   Contact '{name}' added! (ID: {new_contact['id']})")
    return contacts

# ========== VIEW ALL CONTACTS ==========

def view_contacts(contacts):
    print("\n--- ALL CONTACTS ---")
    
    if not contacts:
        print("  No contacts found.")
        return
    
    print("\n" + "-"*95)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<22} {'City':<12} {'Company':<15} {'★':<3}")
    print("-"*95)
    
    for contact in contacts:
        star = "★" if contact.get("favorite", False) else " "
        print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} {contact['email']:<22} {contact['city']:<12} {contact['company']:<15} {star:<3}")
    
    print("-"*95)
    print(f"Total: {len(contacts)} contacts")

# ========== SEARCH CONTACT ==========

def search_contact(contacts):
    print("\n--- SEARCH CONTACT ---")
    print("Search by:")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    
    choice = input("Enter choice (1-3): ")
    keyword = input("Enter search term: ").strip().lower()
    
    results = []
    
    for contact in contacts:
        if choice == "1" and keyword in contact["name"].lower():
            results.append(contact)
        elif choice == "2" and keyword in contact["phone"]:
            results.append(contact)
        elif choice == "3" and keyword in contact["email"].lower():
            results.append(contact)
    
    if results:
        print(f"\n   Found {len(results)} contact(s):")
        for contact in results:
            star = "★" if contact.get("favorite", False) else " "
            print(f"  [{contact['id']}] {contact['name']} - {contact['phone']} - {contact['email']} {star}")
    else:
        print("  No matching contacts found.")

# ========== FILTER CONTACTS ==========

def filter_contacts(contacts):
    print("\n--- FILTER CONTACTS ---")
    print("Filter by:")
    print("1. City")
    print("2. Company")
    
    choice = input("Enter choice (1-2): ")
    filter_value = input("Enter filter value: ").strip().lower()
    
    results = []
    
    for contact in contacts:
        if choice == "1" and contact["city"].lower() == filter_value:
            results.append(contact)
        elif choice == "2" and contact["company"].lower() == filter_value:
            results.append(contact)
    
    if results:
        print(f"\n   Found {len(results)} contact(s):")
        for contact in results:
            star = "★" if contact.get("favorite", False) else " "
            print(f"  [{contact['id']}] {contact['name']} - {contact['city']} - {contact['company']} {star}")
    else:
        print(f"  No contacts found matching '{filter_value}'")

# ========== UPDATE CONTACT ==========

def update_contact(contacts):
    print("\n--- UPDATE CONTACT ---")
    
    if not contacts:
        print("  No contacts to update.")
        return contacts
    
    view_contacts(contacts)
    
    try:
        contact_id = int(input("\nEnter contact ID to update: "))
    except ValueError:
        print("  Invalid ID! Must be a number.")
        return contacts
    
    contact_to_update = None
    for contact in contacts:
        if contact["id"] == contact_id:
            contact_to_update = contact
            break
    
    if not contact_to_update:
        print(f"  Contact with ID {contact_id} not found.")
        return contacts
    
    print(f"\nUpdating: {contact_to_update['name']}")
    print("Press Enter to keep current value.\n")
    
    new_name = input(f"Name [{contact_to_update['name']}]: ").strip()
    if new_name:
        contact_to_update['name'] = new_name
    
    new_phone = input(f"Phone [{contact_to_update['phone']}]: ").strip()
    if new_phone:
        if is_valid_phone(new_phone):
            contact_to_update['phone'] = new_phone
        else:
            print("  Invalid phone! Keeping old value.")
    
    new_email = input(f"Email [{contact_to_update['email']}]: ").strip()
    if new_email:
        if is_valid_email(new_email):
            contact_to_update['email'] = new_email
        else:
            print("  Invalid email! Keeping old value.")
    
    new_city = input(f"City [{contact_to_update['city']}]: ").strip()
    if new_city:
        contact_to_update['city'] = new_city
    
    new_company = input(f"Company [{contact_to_update['company']}]: ").strip()
    if new_company:
        contact_to_update['company'] = new_company
    
    print(f"\n   Contact updated successfully!")
    return contacts

# ========== DELETE CONTACT ==========

def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")
    
    if not contacts:
        print("  No contacts to delete.")
        return contacts
    
    view_contacts(contacts)
    
    try:
        contact_id = int(input("\nEnter contact ID to delete: "))
    except ValueError:
        print("  Invalid ID! Must be a number.")
        return contacts
    
    for i, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            confirm = input(f"Delete '{contact['name']}'? (y/n): ").lower()
            if confirm == 'y':
                deleted = contacts.pop(i)
                print(f"   Deleted: {deleted['name']}")
            else:
                print("  Cancelled.")
            return contacts
    
    print(f"  Contact with ID {contact_id} not found.")
    return contacts

# ========== SORT CONTACTS ==========

def sort_contacts(contacts):
    print("\n--- SORT CONTACTS ---")
    print("1. A to Z (by Name)")
    print("2. Z to A (by Name)")
    print("3. By ID (ascending)")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        contacts.sort(key=lambda x: x["name"].lower())
        print("   Contacts sorted A to Z")
    elif choice == "2":
        contacts.sort(key=lambda x: x["name"].lower(), reverse=True)
        print("   Contacts sorted Z to A")
    elif choice == "3":
        contacts.sort(key=lambda x: x["id"])
        print("   Contacts sorted by ID")
    else:
        print("  Invalid choice")
    
    return contacts

# ========== CSV EXPORT ==========

def export_to_csv(contacts, filename="contacts_export.csv"):
    """Export contacts to CSV file"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Phone", "Email", "City", "Company", "Favorite"])
            for contact in contacts:
                writer.writerow([
                    contact["id"], 
                    contact["name"], 
                    contact["phone"], 
                    contact["email"], 
                    contact["city"], 
                    contact["company"],
                    contact.get("favorite", False)
                ])
        print(f"\n   Contacts exported to {filename}")
    except Exception as e:
        print(f"  Export failed: {e}")

# ========== CSV IMPORT ==========

def import_and_merge(contacts):
    """Import contacts from CSV and merge with existing"""
    filename = input("Enter CSV filename to import (e.g., contacts.csv): ").strip()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            imported_count = 0
            for row in reader:
                # Check if contact already exists by email or phone
                exists = False
                for contact in contacts:
                    if contact["email"] == row["Email"] or contact["phone"] == row["Phone"]:
                        exists = True
                        break
                
                if not exists:
                    new_id = get_next_id(contacts)
                    contacts.append({
                        "id": new_id,
                        "name": row["Name"],
                        "phone": row["Phone"],
                        "email": row["Email"],
                        "city": row["City"],
                        "company": row["Company"],
                        "favorite": row.get("Favorite", "False") == "True"
                    })
                    imported_count += 1
            
        print(f"\n   Imported {imported_count} new contacts from {filename}")
    except FileNotFoundError:
        print(f"  File {filename} not found!")
    except Exception as e:
        print(f"  Import failed: {e}")

# ========== FAVORITES MENU ==========

def favorites_menu(contacts):
    print("\n--- FAVORITES MENU ---")
    print("1. Add to Favorites")
    print("2. View Favorites")
    print("3. Remove from Favorites")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        view_contacts(contacts)
        try:
            contact_id = int(input("Enter contact ID to add to favorites: "))
            for contact in contacts:
                if contact["id"] == contact_id:
                    contact["favorite"] = True
                    print(f"   {contact['name']} added to favorites!")
                    return contacts
            print("  Contact not found")
        except ValueError:
            print("  Invalid ID")
    
    elif choice == "2":
        favorites = [c for c in contacts if c.get("favorite", False)]
        if favorites:
            print("\n--- FAVORITE CONTACTS ---")
            view_contacts(favorites)
        else:
            print("  No favorite contacts found")
    
    elif choice == "3":
        view_contacts(contacts)
        try:
            contact_id = int(input("Enter contact ID to remove from favorites: "))
            for contact in contacts:
                if contact["id"] == contact_id:
                    contact["favorite"] = False
                    print(f"   {contact['name']} removed from favorites!")
                    return contacts
            print("  Contact not found")
        except ValueError:
            print("  Invalid ID")
    
    else:
        print("  Invalid choice")
    
    return contacts