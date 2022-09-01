input_str = input("Enter a list of brackets: ")
char_dict = {"(": ")", "[": "]", "{": "}"}
container = []
def validate(input_str):
    if input_str == "":
        return True
    if len(input_str) % 2 != 0:
        return False
    for char in input_str:
        if char in char_dict:
            container.append(char)
        elif char in char_dict.values():
            if char == char_dict[container.pop()]:
                continue
            else:
                return False
    return True
print(validate(input_str))
    
       
        
