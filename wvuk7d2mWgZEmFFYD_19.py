
def shared_letters(txt1, txt2):
​
    n=len(txt2)
​
    lista=[]
​
    for i in range(0,n):
        if txt2[i] in txt1:
            lista.append(txt2[i])
​
    return len(lista)
​
​
shared_letters("spout", "shout")

