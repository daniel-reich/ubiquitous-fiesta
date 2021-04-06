
letters={"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 2, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
tiles={"-": 1, "DL": 2, "TL": 3, "DW": 1}
​
​
def points(lst, pos, word):
    pts=0
    i=0
    mult=1
    while i<len(word):
        pts+=letters[word[i]]*tiles[lst[pos+i]]
        if lst[pos+i]=="DW":
            mult+=1
        i+=1
    return mult*pts
​
​
def best_start(lst,word):
    word=word.upper()
    arr=[]
    j=0
    while j<len(lst)-len(word)+1:
        curr=points(lst,j,word)
        arr.append(curr)
        j+=1
​
    ind=arr.index(max(arr))
    return ind

