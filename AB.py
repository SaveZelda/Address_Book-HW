import os
import sys

class Contact:
    def __init__(self,first_name,last_name,phone,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
                 
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def edit_phone(self,new_phone):
        self.phone = new_phone
        
    def __repr__(self):
        return "Name: " + self.first_name + self.last_name + " Phone: " + self.phone + " Email: " + self.email
    #"First_name:{0}\nLast_name:{1}\nPhone:{2}\nEmail:{3}".format(self.first_name,self.last_name,self.phone,self.email)
    
    def __del__(self):
        return "Contact for {} deleted".format(self.first_name)
    
    def __eq__(self, other):
        return isinstance(other, Contact) and hash((self.first_name,self.last_name,
                                                    self.phone,self.email)) == hash((other.first_name,other.last_name,other.phone,other.email))
    
    def __hash__(self):
        return hash((self.first_name,self.last_name,elf.phone,self.email))

contacts = list()

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = Contact(contact_data[0],contact_data[1],contact_data[2],contact_data[3])
            contacts.append(contact)

with open("contacts.csv", "w") as f:
    f.write(f"First Name,Last Name,Phone,Email")

def Address_Book():
    users_input = ""
    while users_input != "t":
        print("------------Please Choose Options Below-------------------")
        print("1: Add contact")
        print("2: Display contacts")
        print("3: Find contact")
        print("4: Edit contact phone number")
        print("5: Terminate Program")
        users_input = input("Select option: ")

        if users_input == "1":
            print("Enter your contact's information")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            our_contact = Contact(first_name,last_name,phone,email)
            contacts.append(our_contact)
            print("Contacts created")
        elif users_input == "2":
            print("------------Address Book Display Mode-------------------")
            for contact in contacts:
                print(contact)
            print('Contact Displayed.')
        elif users_input == "3":
            to_lookup = input("Enter contact's first or last name to lookup:\n")
            for contact in contacts:
                if to_lookup in contact.full_name():
                    print(contact)
        elif users_input == "4":
            to_lookup = input("Enter contact's first or last name to lookup:\n")
            for id, contact in enumerate (contacts):
                if to_lookup in contact.full_name():
                    print(id,contact)
            to_edit = input("Which one do you want to change? Enter the respective ID:")
            new_phone = input("What would be the new phone number?")
            contact.edit_phone(new_phone)
            print("------------Changes have been saved. Please see the latest update as below:-------------------")
            print(contact)
            
        elif users_input == "5":
            print("Goodbye!")
            break
            
        else:
            print('Invalid Option! Please choose again!')

        with open("contacts.csv", "w") as f:
            for contact in contacts:
                f.write(f"{contact.first_name},{contact.last_name},{contact.phone},{contact.email}\n")