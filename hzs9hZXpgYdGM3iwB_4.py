
import string
def alternating_caps(txt):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    count = 0
    x = txt.split(' ')
    x[0] = x[0].capitalize()
    newlist = []
    emptystring = ''
    for eachword in x:
        for eachletter in eachword:
            if eachletter in lowercase and count == 1:
                emptystring += eachletter.upper()
                count = 0
            elif eachletter in lowercase and count == 0:
                count = 1
                emptystring += eachletter
            else:
                emptystring += eachletter
                count = 0
        newlist.append(emptystring)
        emptystring = ''
    return ' '.join(newlist)

