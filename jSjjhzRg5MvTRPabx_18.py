
def sentence(words):
    vow = 'aeiou'
​
    def vv(s):
        if s[0] in vow:
            return 'an ' + s
        else:
            return 'a ' + s
​
    buf = [vv(x) for x in words]
    muf = [vv(x) for x in words][0:-1]
    return ', '.join(muf).capitalize() + ' and ' + buf[-1] + '.'

