
def is_sorted(words, alphabet):
    d1={c:i for i,c in enumerate(alphabet)}
    for i in range(len(words)-1):
        word1=words[i]
        word2=words[i+1]
        for k in range(min(len(word1),len(word2))):
            if word1[k]!=word2[k]:
                if d1[word1[k]]>d1[word2[k]]:
                    return False
                break
        else:
            if len(word1)>len(word2):
                return False    
    return True

