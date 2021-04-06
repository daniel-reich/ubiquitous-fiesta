
def make_title(txt):
    #split string up
    list_title = str.split(txt)
    #print(list_title)
    #replace lowercase in list with uppercase
    index = 0
    for i in list_title:
        list_title[index] = str.capitalize(i[:1]) + i[1:]
        index += 1
        #print(list_title)
    #join list back into single string
    return(' '.join(list_title))
    #print(' '.join(list_title))

