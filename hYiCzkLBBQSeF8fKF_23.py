
def count(deck):
    set1={2, 3, 4, 5, 6 }
    set2={7, 8, 9 }
    set3={10, "J", "Q", "K", "A"}
    d=0
    for i in range(0,len(deck),1):
        if deck[i] in set1:
            d=d+1
        elif deck[i] in set2:
            d=d+0
        else:
            d=d-1
    return d
​
result=count(["A", "A", "K", "Q", "Q", "J"])
print(result)

