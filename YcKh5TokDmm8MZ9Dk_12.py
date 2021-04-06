
def strip(txt):
    return [i.lower() for i in txt if ord(i.lower()) in range(97,123)]
def hidden_anagram(text, phrase):
    t=strip(text)
    p=sorted(strip(phrase))
    for i in range(len(t)-len(p)+1):
        if sorted(t[i:i+len(p)])==p:
            return ''.join(t[i:i+len(p)])
    return 'noutfond'

