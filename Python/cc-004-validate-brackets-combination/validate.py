input_str = input("Enter a list of brackets: ")
char_dict = {"(": ")", "[": "]", "{": "}"}
container = []
def validate(input_str):
    if input_str == "":
        return True
    if len(input_str) % 2 != 0:
        return False
    if input_str[0] not in char_dict.keys():
        return False
    for i in input_str:
        if i in char_dict.keys():
            container.append(i)
        elif i in char_dict.values():
            if char_dict[container[-1]] == i:
                container.pop()
            else:
                return False
    return container == []        
print(validate(input_str))
    
       
        
