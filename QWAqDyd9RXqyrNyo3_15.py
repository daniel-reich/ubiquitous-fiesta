
def abbreviate(txt,n=4) :
    output = ""
    crap = txt.split(" ")
    for each in crap :
        if len(each) >= n :
            output += each[0].upper()
    return output

