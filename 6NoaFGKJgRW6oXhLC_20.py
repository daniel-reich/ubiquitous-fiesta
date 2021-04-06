
def sum_of_vowels(txt):
    count = 0
    txt = txt.upper()
    for x in txt:
        if x == "A":
            count += 4
        elif x == "E":
            count += 3
        elif x == "I":
            count += 1
        else:
            count += 0
    return count

