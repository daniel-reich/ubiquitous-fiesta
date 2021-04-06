
def reverse_words(words):
    words = words.lstrip()
    words = words.rstrip()
    split = words.split(" ")
    finalstring = ""
    firstword = split[0]
    index = 1
    reverser = True
    stringmaker = True
    while reverser == True:
        if split[-1] == firstword:
            reverser = False
        else:
            split.insert(0, split[index])
            index += 1
            del split[index]
    while stringmaker == True:
        if not split:
            finalstring = finalstring.lstrip()
            finalstring = finalstring.rstrip()
            stringmaker = False
        else:
            finalstring += split[0] + " "
            del split[0]
    return finalstring

