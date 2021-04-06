
def pig_latin(txt):
    txt1 = ""
    for i in txt:
        if i.isalpha() or i is ' ':
            txt1 = txt1 + i
​
    vowels = "aeiouAEIOU"
    listy = []
    splitty = txt1.split()
​
    for i in splitty:
        if i[0] in vowels:
            listy.append(i+'way')
        else:
            listy.append(i[1::] + i[0:1:]+'ay')
​
    firsty = listy[0].capitalize()
​
    list2 = []
    list2.append(firsty)
    for i in listy[1::]:
        list2.append(i)
    stringy =  (' '.join(list2))
    return stringy+txt[-1]

