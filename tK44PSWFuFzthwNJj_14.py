
def club_entry(word):
    i= sorted([ord(i)-96 for i in word if len(word)>=2 and word.count(i)>=2]) #xd
    return min(i)*4 if i[0]==4 else max(i)*4

