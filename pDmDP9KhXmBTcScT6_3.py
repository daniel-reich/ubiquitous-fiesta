
def get_name(email):
    slovo = ""
    name1 = ""
    name = list(email.split("@"))
    name1 = name[0]
    for character in name1:
        if character.lower() in "abcdefghijklmnopqrstuvwxyz":
            slovo = slovo + character
        else:
            slovo = slovo + ""
    return slovo
​
print(getname("MarkBrull_69@gmail.com"))

