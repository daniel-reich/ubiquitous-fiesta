
def unique_abbrev(abbs, words):
    val = 0
    for i in abbs:
        for word in words:
            if word.startswith(i):
                val += 1
    return val == 3

