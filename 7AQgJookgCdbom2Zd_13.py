
def pig_latin(txt):
    last = txt[-1]
    all_else = txt[0:len(txt)-1]
    txt_list = list()
    for word in all_else.split(' '):
        if word[0].lower() in ['a','e','i','o','u']:
            word2 = word+'way'
        else:
            word2 = word[1:]+word[0]+'ay'
        txt_list.append(word2)
    txt_list[0] = txt_list[0].lower().capitalize()
    #txt_list.append(last)
    return " ".join(str(x) for x in txt_list)+last

