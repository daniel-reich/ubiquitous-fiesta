
def add_letters(a):
    if len(a)==0:return 'z'
    s = sum(list(map(lambda x:ord(x)-96, a)))
    return chr(s+96) if s<=26 else chr(s%26 + 96)

