
def fixisbn(isbn, txt):
    rounded = round(isbn, -1)
    digit = int(txt[12]) + rounded - isbn
    return txt[:12] + str(digit)
​
def isbn10(txt):
    result = "Invalid"
    multiplier = 10
    isbn = 0
    for char in txt:
        if char == "X":
            isbn += 10 * multiplier
        else:
            isbn += int(char) * multiplier
            multiplier-=1
​
    if (isbn%11) == 0:
        txt = "978" + txt
        txt = txt.replace("X","0")
        isbn = getisbn(txt)
        result = fixisbn(isbn,txt)
​
    return result
​
def getisbn(txt):
    isbn = 0
    multiplier = 1
    for char in txt:
        isbn += int(char) * multiplier
        if multiplier == 1:
            multiplier = 3
        else:
            multiplier = 1
    return isbn
​
def isbn13(txt):
    isbn = 0
    if len(txt) == 10:
        return isbn10(txt)
    else:
        isbn = getisbn(txt)
        return "Valid" if (isbn%10==0) else "Invalid"

