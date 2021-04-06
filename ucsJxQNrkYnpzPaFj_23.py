
def char_appears(sentence, char):
    finallist=[]
    for words in str.lower(sentence).split():
        count=0
        for letter in words:
            if letter == str.lower(char):
                count+=1
        finallist.append(count)
    return finallist

