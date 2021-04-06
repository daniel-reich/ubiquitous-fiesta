
def letters_only(s):
    if s == "":
        return(False)
    for i in s:
        if i.islower() == True or i == " ":
            continue
        else:
            return(False)
    return(True)

