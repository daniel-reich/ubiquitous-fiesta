
def duplicates(txt):
    templist = []
    counter = 0
    for letters in txt:
        if letters not in templist:
            templist.append(letters)
        else:
            counter += 1
    return counter

