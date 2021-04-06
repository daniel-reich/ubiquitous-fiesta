
def max_ham(s1, s2):
    count=0
    if len(s1)!=len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i] not in s2:
            return False
        elif s1[i]!=s2[i]:
            count+=1
    if count==len(s1):
        return True
    else:
        return count

