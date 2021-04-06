
def reverse_sort(txt):
    words = txt.split()
    ans = sorted(words,key = lambda x:(len(x),x.lower(),-ord(x[0])))
    return ' '.join(ans[::-1])

