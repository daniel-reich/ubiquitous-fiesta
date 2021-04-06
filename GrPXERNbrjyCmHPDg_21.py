
def duplicate_count(txt):
    letters = {}
    count = 0
    for i in txt:
        letters[i] = txt.count(i)
    letters = {key: value for (key, value) in letters.items() if value > 1 } #List Comprehension
    return(len(letters))

