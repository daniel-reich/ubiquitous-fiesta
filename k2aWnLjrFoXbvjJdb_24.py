
from collections import deque
def vigenere(text, keyword):
    alphabet="".join([chr(i) for i in range(65,91)])    
    compare=(len(text)//len(keyword)+1)*keyword.upper()
    if " " in text:
        text="".join([char for char in text if char.isalpha()]).upper()
        res,ind="",0
        for char in text:
            search_index=alphabet.index(text[ind])+1
            col_num=alphabet.index(compare[ind])+1        
            d=deque(alphabet)
            d.rotate(-col_num+1)
            res+=d[search_index-1]
            ind+=1
        return res
    else:
        res,ind="",0
        for char in text:
            d=deque(alphabet) 
            col_num=alphabet.index(compare[ind])
            d.rotate(-col_num)
            d=list(d)
            search_index=d.index(text[ind])
            res+=alphabet[search_index]
            ind+=1
        return res

