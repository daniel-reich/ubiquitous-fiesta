
def isWordChain(words):
    idx1, idx2 = 0, 1 
​
    while idx2 < len(words):
        w1 = words[idx1]
        w2 = words[idx2]
​
        if abs(len(w1) - len(w2)) > 1:
            return False
        
        if abs(len(w1) - len(w2)) == 0:
            sameCount = 0
            i = 0
            while i < len(w1):
                if w1[i] == w2[i]:
                    sameCount += 1
                i += 1
            if len(w1) - sameCount > 1:
                return False
        
        elif abs(len(w1) - len(w2)) == 1:
            found = False
            i = 0
            
            if len(w1) < len(w2):
                while i < len(w2):
                    wordCheck = ''
                    j = 0
                    while j < len(w2):
                        if j != i:
                            wordCheck += w2[j]
                        j += 1
​
                    if wordCheck == w1:
                        found = True
                        break
                    i += 1
                
                if found == False:
                    return False
            
            else:
                while i < len(w1):
                    wordCheck = ''
                    j = 0
                    while j < len(w1):
                        if j != i:
                            wordCheck += w1[j]
                        j += 1
                    
                    if wordCheck == w2:
                        found = True
                        break
                    i += 1
                
                if found == False:
                    return False
​
        idx1 += 1
        idx2 += 1
​
    return True

