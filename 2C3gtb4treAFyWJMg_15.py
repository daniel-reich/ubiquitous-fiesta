
def decode(data):
    a="a b c d e f g h i k l m n o p q r s t u v w x y z"
    alphabet=a.split()
    sentence=""
    for i in range(len(data)):
        word=""
        for j in range(0,len(data[i])-1,2):
            n=data[i][j:j+2]
            n=list(str(n))
            letter=alphabet[((int(n[0])-1)*5+int(n[1]))-1]
            word=word+letter
        sentence=sentence+word+" "
    #print(sentence)
    return sentence[:-1]
​
​
def encode(data):
    a=[["a", "b", "c" ,"d", "e"],[ "f", "g", "h", "i", "k"],[ "l", "m" ,"n" ,"o" ,"p"], ["q", "r", "s", "t", "u"],[ "v", "w", "x", "y", "z"]]
    newsentence=""
    for i in range(len(data)):
        word=data[i].lower()
        newword=""
        for j in range(len(word)):
            letter=word[j]
            if(letter=="'"):
                tmp=1
                #do nothing
            elif(letter=="j"):
                letter="i"
                for k in range(len(a)):
                    for l in range(len(a[0])):
                        if(a[k][l]==letter):
                            newletter=str(k+1)+str(l+1)
                            newword=newword+newletter
            else:
                for k in range(len(a)):
                    for l in range(len(a[0])):
                        if(a[k][l]==letter):
                            newletter=str(k+1)+str(l+1)
                            newword=newword+newletter
                            break
​
        newsentence=newsentence+newword+" "
    #print(newsentence)
    return newsentence[:-1]
​
def polybius(message):
    data=message.split()
    if(data[0].isnumeric()):
​
        return decode(data)
    else:
        return encode(data)

