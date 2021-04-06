
def superheroes(heroes):
    words_list=[]
    for word in heroes:
        if  word[-3:]=="man" and word[-4]!="o":
            words_list.append(word)
    words_list.sort()
    return words_list

