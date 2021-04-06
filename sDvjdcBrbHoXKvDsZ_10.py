
def anagram(name, words):
    nameDict={}
    wordsDict={}
    name=name.lower()
    for i in name :
        if i in nameDict :
            nameDict[i]+=1
        else:
            nameDict[i]=1
    del nameDict[' ']
    for word in words:
        for j in word:
            if j in wordsDict:
                wordsDict[j] += 1                
            else:
                wordsDict[j] = 1
  
    return nameDict == wordsDict

