
def sentence(words):
    ans =''
    for i, w in enumerate(words):
        if w[0] in 'aeiou':
            pre = 'an '
        else:
            pre = 'a '
        if i == len(words) - 1:
            beg = ' and '
        elif i == 0:
            beg = ''
        else:
            beg = ', '
        ans += beg + pre + w
    ans += '.'
    return ans.capitalize()

