
def correct_sentences(s):
    s = [i.strip() for i in s.split()]
    s[0] = s[0].capitalize()
    for i in range(1, len(s)):
        if s[i][0].isupper():
            s[i-1] +='.'
    return ' '.join(s) + '.'

