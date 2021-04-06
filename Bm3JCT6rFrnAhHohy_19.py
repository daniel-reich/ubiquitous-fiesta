
def alphabet_index(txt):
    alpha = "abcdefghijklmnopqrstuvwxyz"
​
    array = []
    for i in txt.lower():
        if i in alpha:
            array.append(alpha.index(i))
​
    answer = [x + 1 for x in array]
    answer = [str(i) for i in answer]
​
    return " ".join(answer)

