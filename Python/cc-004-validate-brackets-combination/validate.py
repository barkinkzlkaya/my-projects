input_str = input("Enter a list of brackets: ") # user input
char_dict = {"(": ")", "[": "]", "{": "}"} # dictionary for brackets
container = [] # container for brackets
def validate(input_str):
    if input_str == "": # if input is empty return true
        return True
    if len(input_str) % 2 != 0: # if input has odd number of brackets return false
        return False
    if input_str[0] not in char_dict.keys(): # if first character is not a open bracket return false
        return False
    for i in input_str:
        if i in char_dict.keys(): # if character is an open bracket add to container
            container.append(i)
        elif i in char_dict.values():  # if character is a close bracket and it match the last element in container remove it from container
            if char_dict[container[-1]] == i: 
                container.pop() 
            else:
                return False
    return container == []    # if container is empty return true else return false     
print(validate(input_str)) # print result of validate function
    
       
        
