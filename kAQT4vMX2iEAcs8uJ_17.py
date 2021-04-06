
def longest_7segment_word(lst):
    banned_letters = ['k','m','v','w','x']
    x = [word for word in lst if not any(i in banned_letters for i in word)]
    if not x:
        return ''
    else: return max(x, key=len)

