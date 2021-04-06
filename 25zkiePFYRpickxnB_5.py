
def count_boomerangs(v):
    count=0
    for i in range(len(v)):
        s=v[i:i+3]
        if len(s)==3:
            if s[0]==s[2] and s[1]!=s[0]:
                count+=1
    return count

