def surname_use():
    fam = input("Enter the contact's last name: ")
    return fam


def name_use():
    name = input("Enter the name of the contact: ")
    return name


def telephon_use():
    tel = input("Enter the contact's phone number: ")
    return tel


def description_use():
    desc = input("Enter a description for the contact: ")
    return desc


def data_collection():
    return (surname_use(), name_use(), telephon_use(), description_use())
