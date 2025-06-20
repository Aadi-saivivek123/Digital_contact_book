from modules.contact import Contact  
class ContactBook:  
    Filename= "data\contacts.txt"
    def __init__(self): 
        self.contacts=[]  
        self.load_contacts()
    def add_contact(self,name,phone,email): 
        new_contact=Contact(name,phone,email) 
        self.contacts.append(new_contact) 
        self.save_contacts() 
        print("New contact successfully added") 
    def view_contacts(self): 
        if not self.contacts: 
            print("No contacts available") 
        else: 
            print("contacts available") 
        for contact in self.contacts: 
            contact.contact_info() 
    def delete_contact(self,name_of_person): 
        for contact in self.contacts: 
            if(contact.name==name_of_person): 
                self.contacts.remove(contact)  
                self.delete_file_contact()
                print('Contact deleted successfully')
                return 
        print("Contact not found") 
    def save_to_file(self):  
        with open(self.Filename,'w') as f:  
            for contact in self.contacts: 
                f.write(f"{contact.name},{contact.phone},{contact.email}\n") 
    def load_contacts(self):  
        with open(self.Filename,'r') as f: 
            for line in f: 
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name,phone_number,email=parts 
                    contact = Contact(name, int(phone_number), email)
                    self.contacts.append(contact) 
    def save_contacts(self):
        with open(self.Filename, "w") as file:
            for contact in self.contacts:
                line = f"{contact.name},{contact.phone},{contact.email}\n"
                file.write(line) 
    def delete_file_contact(self): 
        with open(self.Filename, "w+") as file: 
            for contact in self.contacts:
                line = f"{contact.name},{contact.phone},{contact.email}\n"
                file.write(line)


  
            

