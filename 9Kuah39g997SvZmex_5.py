
def common_last_vowel(x):
    c = x.split()
    lst = [i[-1].lower() for i in c if i[-1].lower() in 'aeiou']
    if len(lst)==0:
        lst2 = [j.lower() for i in c for j in i if j in 'aeiou']
        return sorted(lst2)[-1]
    else:
        return sorted(lst)[-1]

