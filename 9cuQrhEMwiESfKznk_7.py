
def eng2nums(s):
    names = ['zero','one','two','three','four','five','six','seven','eight','nine',
        'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
        'eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy',
        'eighty','ninety','hundred']
    n = 0
    for w in s.split():
        x = names.index(w)
        if x == 28:
            n *= 100
        else:
            n += x if x < 21 else 10 * (x - 18)
    return n

