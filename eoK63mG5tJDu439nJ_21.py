
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)
​
def isWordChain(words):
    
    leven= []
    for i in range(len(words)-1):
        leven.append((words[i],words[i+1]))    
    for i in leven:
        (a,b) = i
        if not a: return len(b)
        if not b: return len(a)
        if min(levenshtein(a[1:], b[1:])+(a[0] != b[0]), levenshtein(a[1:], b)+1, levenshtein(a, b[1:])+1)>1: return False
    return True

