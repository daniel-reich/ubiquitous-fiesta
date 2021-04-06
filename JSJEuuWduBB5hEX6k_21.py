
def XO(txt):
    x = 0
    o = 0
    for elem in txt:
        if elem == "x" or elem == "X":
            x += 1
        elif elem == "o" or elem == "O":
            o += 1
    if x == o:
        return True
    else:
        return False
​
test = XO("oxoxxxxxxx")
​
print(test)

