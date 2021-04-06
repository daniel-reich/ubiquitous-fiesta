
def edit_words(arr):
    x = [j[::-1] for j in [i.upper() for i in arr]]
    y = [i[:len(i)//2]+'-'+i[len(i)//2:] if len(i) %
         2 == 0 else i[:len(i)//2+1]+'-'+i[len(i)//2+1:] for i in x]
​
    return y

