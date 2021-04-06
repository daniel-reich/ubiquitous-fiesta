
def generate_palindromes(limit):
    lst = []
    l = list(range(limit+1))
    l.reverse()
    for i in l:
        if len(lst) < 15:
            if str(i) == str(i)[::-1]:
                lst.append(i)
    lst = sorted(lst)
    return lst

