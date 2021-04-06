
def vowels(string):
    if len(string) == 0: 
        return 0
    elif string[0] in ["a", "u", "e", "o", "i"]: 
        return 1 + vowels(string[1:])
    else : 
        return vowels(string[1:])

