
def get_missing_letters(s):
​
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    return ''.join([i for i in letters if not i in s])

