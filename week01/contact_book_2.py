import json

CONTACTS_FILE = "contacts.json"

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def add_contact(contacts, name, phone):
    if name in contacts:
        print(f"Overwriting existing number for {name} ({contacts[name]}).")
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Saved {name}: {phone}")

def lookup_contact(contacts, name):
    phone = contacts.get(name)
    if phone is None:
        print(f"No contact named {name}.")
    else:
        print(f"{name}: {phone}")

def delete_contact(contacts, name):
    if name not in contacts:
        print(f"No contact named {name}.")
        return
    del contacts[name]
    save_contacts(contacts)
    print(f"Deleted {name}.")

if __name__ == "__main__":
    contacts = load_contacts()
    print(f"Loaded {len(contacts)} contact(s).")

    while True:
        print("\n1. Add 2. Look up 3. Delete 4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(contacts, name, phone)
        elif choice == "2":
            lookup_contact(contacts, input("Name: "))
        elif choice == "3":
            delete_contact(contacts, input("Name: "))
        elif choice == "4":
            break
        else:
            print("Not a valid choice.")

