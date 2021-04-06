
def polybius(text):
    info = ["abcde","fghik","lmnop","qrstu","vwxyz"]
    abc = "abcdefghiklmnopqrstuvwxyz"
    r = ""
    if "0"<=text[0]<="9":
        i=0
        while i<len(text):
            if "0"<=text[i]<="9":
                r+=info[int(text[i])-1][int(text[i+1])-1]
                i+=2
            else:
                r+=" "
                i+=1
    else:
        text= text.lower().replace("j","i")
        for e in text:
            if e in abc:
                r+=str((abc.find(e))//5+1)
                r+= (str((abc.find(e)+1)%5) if (abc.find(e)+1)%5!=0 else str(5))
            elif e==" ":
                r+=" "
            else:
                r+=""
    return r

