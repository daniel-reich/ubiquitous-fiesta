
def syllabification(word):
    v = ['a', 'A', 'e', 'i', 'o', 'u']
​
    ans = ''
    end = len(word)
    wrds = []
    for i in range(len(word) -1, -1, -1):
        if(word[i] in v):
            wrds.append(word[i-1:end])
            end = i-1
​
    wrds.reverse()
    for w in wrds:
        ans = ans + w + '.'
    
    return ans[:-1]

