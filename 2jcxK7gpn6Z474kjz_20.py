
def security(txt):
    theif = False
    money = False
    for letter in txt:
        if letter == "T" and money:
            return "ALARM!"
        elif letter == "T":
            theif = True
        elif letter == "G":
            money = False
            theif = False
        elif letter == "$" and theif:
            return "ALARM!"
        elif letter == "$":
            money = True
    return "Safe"

