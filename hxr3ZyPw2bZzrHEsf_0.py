
def make_title(txt):
    lst = [word[0].upper() + word[1:] for word in txt.split(' ')]
    ans = ' '.join(lst)
    return ans

