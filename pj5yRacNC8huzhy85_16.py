
def shhh(txt):
    myTxt = "\", whispered Edabit."
​
    lst = []
    word_count = 1
    for word in txt.split():
        if word_count == 1:
            lst.append(word.title())
        else:
            lst.append(word.lower())
        word_count += 1
​
    return '"' + " ".join(lst) + myTxt

