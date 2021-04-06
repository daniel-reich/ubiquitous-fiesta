
def word_builder(ltr, pos):
 z=len(ltr)
 print(z)
 z=int(z)
 i=0
 word=str()
 while i<z:
    x=pos[i]
    x=int(x)
    print(x)
    y=ltr[x]
    word=word+str(y)
    i+=1
 return(word)

