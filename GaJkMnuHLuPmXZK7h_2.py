
def letters(word1, word2):
    count_common=''
    count_word2=''
    count_word1=''
    m=sorted(list(set(word1)))
    n=sorted(list(set(word2)))
    
    for i in n:
        if i in m:
            
            count_common +=i
        else:
            count_word2 +=i
    for j in m:
        if j not in n:
            count_word1 +=j
    return [count_common,count_word1,count_word2]

