
def shared_letters(txt1, txt2):
    input = list(dict.fromkeys(list(txt1)))
    count = 0
    for i in input:
        for j in txt2:
            if i == j:
                count += 1
    return count

