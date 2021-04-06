
def next_letters(s):
    if s.count('Z')==len(s):
        return 'A'*(len(s)+1)
    for i in range(len(s)-1,-1,-1):
        x=chr(ord(s[i])+1)
        if x!='[':
            return s[:i]+x+s[i+1:]
        else:
            s=s[:i]+'A'+s[i+1:]
    return s

