
def welcome():
    userinput = int(input("""Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : """))
    return userinput

def phonebook():
    dictionary = {}
    
    while True:
        userinput = welcome()
        
        if userinput == 1:
                name = input("Find the phone number of :")
                if name in dictionary:
                    print(dictionary[name])
                else:
                    print("Couldn't find phone number of ",name) 
                    
        elif userinput == 2:
            try:
                contact_name = input("Insert name of the person : ")
                phone_number = int(input("Insert phone number of the person: "))
            
                if phone_number not in dictionary.items():
                    dictionary.update({contact_name:phone_number})
                    print('Phone number of', contact_name,  'is inserted into the phonebook')
                else : 
                    print("This contact already exist!")
            except ValueError as error:
                print('Invalid input format, cancelling operation ...')        
                
        elif  userinput == 3:
            name = input("Whom to delete from phonebook : ")
            if name in dictionary:
                dictionary.pop(name,None)
                print(name, 'is deleted from the phonebook')
            else: 
                print("This contant does not exist! ")    
                      
        elif userinput == 4:
            print('Exiting Phonebook') 
            break
        else:
            print('Incorrect Entry')         
phonebook()