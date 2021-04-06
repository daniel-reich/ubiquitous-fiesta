
def shift_letters(text,n):
    n = n%(len(text))
    spaces=[]
    for i in text:
        if i ==" ":
            spaces.append(text.index(i))
            text=text.replace(" ","*",1)
    # print(spaces)
    text = text.replace("*","")
    # print(text)
    l = len(text)
    n = n%(len(text))
    text = text[l-n:] + text[:l-n]
    # print(text,n,l)
    for i in spaces:
        text=text[0:i]+ " " + text[i:]
        # print(text)
    return text

