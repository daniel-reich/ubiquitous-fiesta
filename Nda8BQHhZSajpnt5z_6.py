
def GCD(lst):
    counter = min(lst)
    while True:
        rest = [i%counter for i in lst]
        if rest.count(0) == len(rest):
            return counter
        else:
            counter -= 1

