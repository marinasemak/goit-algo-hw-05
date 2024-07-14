from errors_handler import input_error


# add new contact to the dictionary
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# change phone for existed contact
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact not found"


# show phone of existed contact
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name} {contacts[name]}"
    else:
        return "Contact not found"


# show all contacts from the dictionary
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
