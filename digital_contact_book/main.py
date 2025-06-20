from modules.contact_book import ContactBook
book =ContactBook()   
while True:   
    print("\n--- DIGITAL CONTACT BOOK ---")
    print("1. Add_Contact")
    print("2. View_Contacts")
    print("3. Delete_Contact")
    print("4. Exit") 
    user_choice=int(input("\nEnter a number of your choice:"))
    if(user_choice==1): 
        name=input("Enter your name:").strip().capitalize() 
        if(name.isalpha()): 
            pass 
        else:  
            print("Invalid name") 
            continue
        number=input("Enter your mobile number:") 
        if(number.isdigit() and len(number)==10):  
            number=int(number)
            pass 
        else:  
            print("Invalid mobile number")
            continue
        email=input("Enter your email:") 
        if(email.endswith("@gmail.com") and len(email)>10): 
            pass 
        else:  
            print("Invalid email_id")
            continue
        book.add_contact(name,number,email) 
    elif(user_choice==2):  
        book.view_contacts() 
    elif(user_choice==3): 
        name = input("Enter the name you want to delete:")  
        if(name.isalpha()): 
            pass 
        else:  
            print("Invalid name") 
            continue
        book.delete_contact(name) 
    elif(user_choice==4): 
        break  
    else: 
        print("Invalid input")