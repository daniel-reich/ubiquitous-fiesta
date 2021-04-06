
def special_reverse_string(txt):
    rev=[]
    temp=[]
    result=""
    for char in txt:
        temp.append(char)
    for i in temp:
        if i!=" ":
            rev.insert(0,i.lower())
    for j in range(len(temp)):
        if temp[j].isupper():
            rev[j]=rev[j].upper()
        if temp[j]==" ":
            rev.insert(j," ")
    for i in rev:
        result+=i
​
    return result

