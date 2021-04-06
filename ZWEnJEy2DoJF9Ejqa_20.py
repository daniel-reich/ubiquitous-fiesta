
def edabit_in_string(txt):
    word=[x for x in txt]
    find=list('edabit')
    index_check=(list(enumerate(txt)))
    word_index=[]   
    for x in find:
        if x not in word:
            return "NO"
        else:
            if word_index:
                if word.index(x)>word_index[-1]:
                    word_index.append(word.index(x))
                else:                    
                    list1=[y[0] for y in index_check if y[1]==x and y[0]>word_index[-1]]
                    if list1:
                        word_index.append(list1[0])
                    else:
                        return "NO"
            else:
                word_index.append(word.index(x))  
    if len(word_index)!=6 or sorted(word_index)!=word_index:
        return "NO"
    return "YES"

