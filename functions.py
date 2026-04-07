import re

def is_valid_email(email): # this function is used to check the validation of an email.
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):  # this funtion is used to validate the phone no.
    return phone.isdigit() and len(phone) >= 10

def get_next_id(contacts): # for generating the unique ID for each contact.
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

       # FOR ADDING CONTACTS.......
def add_contact(contacts): 
    print("\n--- ADD NEW CONTACT ---")
    
    while True:
        name = input("Full Name: ").strip() # I used strip function to remove extra spaces.
        if name:
            break
        print("Name cannot be empty!")
    
    while True:
        phone = input("Phone Number: ").strip()
        if is_valid_phone(phone):
            break
        print("Invalid! Must be at least 10 digits, numbers only.")
    
    while True:
        email = input("Email Address: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email! Example: name@domain.com")
    
    while True:
        city = input("City: ").strip()
        if city:
            break
        print("City cannot be empty!")
    
    while True:
        company = input("Company: ").strip()
        if company:
            break
        print("Company cannot be empty!")


    # it creates a dictionary for new contact
    new_contact = {
        "id": get_next_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "company": company
    }
    
    contacts.append(new_contact)  # adds new contact to the list of contacts.
    print(f"\n[OK] Contact '{name}' added! (ID: {new_contact['id']})")
    
    return contacts

# FOR VIEWING ALL CONTACTS......

def view_contacts(contacts):
    print("\n--- ALL CONTACTS ---")
    
    if not contacts:
        print("No contacts found.")
        return
    # this is for printing table.
    print("\n" + "-"*85)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<20} {'City':<12} {'Company':<15}")
    print("-"*85)
    # for loop to print each contact and its details.
    for contact in contacts:
        print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} {contact['email']:<20} {contact['city']:<12} {contact['company']:<15}")
    
    print("-"*85)
    print(f"Total: {len(contacts)} contacts")



#FOR SEARCHING CONTACTS.....
def search_contact(contacts): # THIS function gives the users choice like how they want to search the contact.
    print("\n--- SEARCH CONTACT ---")
    print("Search by:")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    
    choice = input("Enter choice (1-3): ")
    keyword = input("Enter search term: ").strip().lower()   # lower fuction is for making case insensitive.
    
    results = []
    
    if choice == "1":
        for contact in contacts:
            if keyword in contact["name"].lower():
                results.append(contact)
    elif choice == "2":
        for contact in contacts:
            if keyword in contact["phone"]:
                results.append(contact)
    elif choice == "3":
        for contact in contacts:
            if keyword in contact["email"].lower():
                results.append(contact)
    else:
        print("Invalid choice!")
        return
    
    if results: # for displaying the result.
        print(f"\n[OK] Found {len(results)} contact(s):")
        for contact in results:
            print(f"  [{contact['id']}] {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("[ERROR] No matching contacts found.")   


#FOR FILTERING THE CONTACTS....
def filter_contacts(contacts):
    print("\n--- FILTER CONTACTS ---")
    print("Filter by:")
    print("1. City")
    print("2. Company")
    
    choice = input("Enter choice (1-2): ")
    filter_value = input("Enter filter value: ").strip().lower()
    
    results = []
    
    if choice == "1":
        for contact in contacts:
            if filter_value == contact["city"].lower():
                results.append(contact)
    elif choice == "2":
        for contact in contacts:
            if filter_value == contact["company"].lower():
                results.append(contact)
    else:
        print("Invalid choice!")
        return
    
    if results:
        print(f"\n[OK] Found {len(results)} contact(s):")
        for contact in results:
            print(f"  [{contact['id']}] {contact['name']} - {contact['city']} - {contact['company']}")
    else:
        print("[!] No contacts found.")




# FOR UPDATING THE CONTACTS....
def update_contact(contacts):
    print("\n--- UPDATE CONTACT ---")
    
    if not contacts:
        print("No contacts to update.")
        return contacts
    
    view_contacts(contacts)
    
    try:   # ERROR handling.
        contact_id = int(input("\nEnter contact ID to update: "))
    except ValueError:
        print("Invalid ID!")
        return contacts
    
    contact_to_update = None
    for contact in contacts:
        if contact["id"] == contact_id:
            contact_to_update = contact
            break
    
    if not contact_to_update:
        print(f"Contact with ID {contact_id} not found.")
        return contacts
    
    print(f"\nUpdating: {contact_to_update['name']}")
    print("Press Enter to keep current value.")
    
    new_name = input(f"Name [{contact_to_update['name']}]: ").strip()
    if new_name:
        contact_to_update['name'] = new_name
    
    new_phone = input(f"Phone [{contact_to_update['phone']}]: ").strip()
    if new_phone:
        if is_valid_phone(new_phone):
            contact_to_update['phone'] = new_phone
        else:
            print("Invalid phone! Keeping old value.")
    
    new_email = input(f"Email [{contact_to_update['email']}]: ").strip()
    if new_email:
        if is_valid_email(new_email):
            contact_to_update['email'] = new_email
        else:
            print("Invalid email! Keeping old value.")
    
    new_city = input(f"City [{contact_to_update['city']}]: ").strip()
    if new_city:
        contact_to_update['city'] = new_city
    
    new_company = input(f"Company [{contact_to_update['company']}]: ").strip()
    if new_company:
        contact_to_update['company'] = new_company
    
    print(f"\n[OK] Contact updated successfully!")
    return contacts





# FOR DELETING THE CONTACT.....
def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")
    
    if not contacts:
        print("No contacts to delete.")
        return contacts
    
    print("Delete by:")
    print("1. ID")
    print("2. Name")
    
    choice = input("Enter choice (1-2): ")
    
    if choice == "1":
        try:
            contact_id = int(input("Enter contact ID to delete: "))
        except ValueError:
            print("Invalid ID!")
            return contacts
        
        for i, contact in enumerate(contacts):
            if contact["id"] == contact_id:
                confirm = input(f"Delete '{contact['name']}'? (y/n): ").lower()
                if confirm == 'y':
                    deleted = contacts.pop(i)
                    print(f"[OK] Deleted: {deleted['name']}")
                return contacts
        print(f"Contact with ID {contact_id} not found.")
    
    elif choice == "2":
        name = input("Enter name to search: ").strip().lower()
        
        results = []
        for contact in contacts:
            if name in contact["name"].lower():
                results.append(contact)
        
        if not results:
            print("No matching contacts found.")
            return contacts
        
        print("\nMatching contacts:")
        for contact in results:
            print(f"  [{contact['id']}] {contact['name']}")
        
        try:
            contact_id = int(input("\nEnter ID of contact to delete: "))
        except ValueError:
            print("Invalid ID!")
            return contacts
        
        for i, contact in enumerate(contacts):
            if contact["id"] == contact_id:
                confirm = input(f"Delete '{contact['name']}'? (y/n): ").lower()
                if confirm == 'y':
                    deleted = contacts.pop(i)
                    print(f"[OK] Deleted: {deleted['name']}")
                return contacts
        print(f"Contact with ID {contact_id} not found.")
    
    else:
        print("Invalid choice!")
    
    return contacts


