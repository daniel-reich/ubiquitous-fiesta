
d = {}
for i in range(0, 10):
    d[str(i)] = i
​
import string
​
for a, b in enumerate(string.ascii_lowercase):
    d[b] = a+1 
​
​
def sentence_primeness(sentence):
    lst = []
    s  = ""
    for i in sentence:
        if i.isspace() and s != "":
            lst.append(s)
            s = ""
        if i.lower() in d.keys():
            s += i
    lst.append(s)
    total = 0
    
    for i in lst:
        total += wordValue(i)
    
    print(total)
    if isPrime(total):
        return "Prime Sentence"
    
    lstSums = [(total - wordValue(i)) for i in lst]
    
    for a, b in enumerate(lstSums):
        if isPrime(b):
            return "Almost Prime Sentence ({})".format(lst[a])
    else:
        return "Composite Sentence"
​
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    else:
        return True
​
def wordValue(word):
    return sum([d[i.lower()] for i in word])

