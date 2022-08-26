#Create empty list
list = []

#While loop to get the list of numbers from the user separated by spaces

while True:
    # Get the list of numbers from the user separated by spaces
    list = input("Enter a list of numbers separated by spaces: ")
    
    # Exit the program if the user types "exit"
    if list.lower() == "exit":
        print("Exiting the program... Good Bye")
        exit()
    
    else :
        try:
            # Convert the list of numbers into a list of integers
            list = [int(x) for x in list.split()]  
        
        # If the user enters a non-integer, print an error message and continue the loop    
        except ValueError:
            print("Not Valid Input, Please enter a list of numbers separated by spaces")
            continue
        
        else :
            # Turn the list into a ordered one
            list = sorted(list)  
            
            # Print the largest number

            print("The largest number is: ", list[-1])  