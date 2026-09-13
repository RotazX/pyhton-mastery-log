
def add_contact(contacts, name, phone):
    if name in contacts:
        print(f"Overwriting existing number for {name} ({contacts[name]}).")
    contacts[name] = phone
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
    print(f"Deleted {name}.")

if __name__ == "__main__":
    contacts = {}

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