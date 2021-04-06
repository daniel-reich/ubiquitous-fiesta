
def no_duplicate_letters(phrase):
    words = phrase.split(' ')
    boolean = True
    for i in words:
        for j in i:
            if i.count(j) > 1:
                boolean = False
    return boolean

