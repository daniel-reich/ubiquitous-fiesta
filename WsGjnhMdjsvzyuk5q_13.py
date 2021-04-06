
def dashed(txt):
    return ''.join(['-' + x + '-' if x in 'aeiouAEIOU' else x for x in txt])

