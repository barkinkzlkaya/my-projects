import random


while True:
    full_name = input("Enter your full name: ")
    full_name = full_name.lower()
    numbers = [0,1,2,3,4,5,6,7,8,9]
    if full_name == "exit":
        break
    else :
        def generate_password():
            password = []
            for i in range(3):
                password.append(random.choice(full_name))
            for x in range (4):
                password.append(str(random.choice(numbers)))
            str_pass = ''.join([str(elem) for elem in password])
            print (str_pass)
        
    generate_password()    