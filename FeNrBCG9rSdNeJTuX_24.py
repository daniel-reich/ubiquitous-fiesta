
def max_possible(n1, n2):
    s=sorted([int(e) for e in str(n2)],reverse=True)
    n1=[int(e) for e in str(n1)]
    j=0
    for i in range(len(n1)):
        if j>=len(s):
            break
        if s[j]>n1[i]:
            n1[i]=s[j]
            j+=1
    return int("".join([str(e) for e in n1]))

