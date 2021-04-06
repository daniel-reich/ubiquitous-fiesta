
def translate_word(word):
    vowels=['a','e','i','o','u']
    res,x='',[]
    a=word
    word=word.lower()
    if len(word)==0:
        return word
    if word[0] in vowels:
        res=word+'yay'
        if a[0].isupper():
            return res.title()
        else:
            return res
    else:
        for i,v in enumerate(word):
            if v in vowels:
                res+=word[i:]+word[:i]+'ay'
                x.append(res)
                res=''
        if a[0].isupper():            
            return x[0].title()
        else:return x[0]
def translate_sentence(sentence):
    vowels=['a','e','i','o','u']
    if len(sentence)==0:
        return sentence
    a=sentence.split()
    x,b=[],[]
    sentence=sentence.replace(',','').replace('"','').replace('?','').lower().split()
    for word in sentence:
        if word[0] in vowels :
            x.append(word+'yay')    
        else:
            for i,v in enumerate(word):
                if v in vowels:
                    b.append(word[i:]+word[:i]+'ay')
            x.append(b[0])
            b=[]
    if a[-1]=='end?"': 
        x[0]=x[0].title()
        x[1]=x[1]+','
        x[2]='"'+x[2].title()
        x[-1]=x[-1]+'?'+'"'
        return ' '.join(x)    
    if  x[-1]=='odaytay':
        x[-1]=x[-1].replace('odaytay','odaytay?')
        x[0]=x[0].title()
        return ' '.join(x)
    if a[0].isupper():
        x[0]=x[0].title()
        return ' '.join(x)

