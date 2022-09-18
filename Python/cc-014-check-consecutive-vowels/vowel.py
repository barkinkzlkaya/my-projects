while True:
    print("Enter '0' for exit.")
    user_entry = input("Please enter a string: ")
    positive = "Positive"
    negative = "Negative"
    def consecutive_vowels(user_entry):
        vowels = "aeiouıöü"
        if user_entry == "0":
            exit()
        for i in range(len(user_entry)):
            if len(user_entry) < 2:
                return negative
            if user_entry[i] in vowels:
                if user_entry[i+1] in vowels:
                    return positive
                else:
                    return negative
    print(consecutive_vowels(user_entry))        