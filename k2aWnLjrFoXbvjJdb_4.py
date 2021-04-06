
def vigenere(text, keyword):
    alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    trs='';p=0
    text=text.upper() 
    keyword=keyword.upper()*int(len(text)/len(keyword)+len(keyword))
    if chr(32) in text:
        text=text.replace(' ','')
        text=text.replace("'","")
        for i in text:
            if i in alf:
                trs+=alf[ord(text[p])+ord(keyword[p])-130]
                p+=1
    else:
        for i in text:
            trs+=alf[ord(text[p])-ord(keyword[p])+26]
            p+=1
    return trs

