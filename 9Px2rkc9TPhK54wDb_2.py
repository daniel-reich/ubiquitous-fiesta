
def ecg_seq_index(n):
    seq=[1,2]
    i=1
    while(n not in seq):
        while(True):
            if(i in seq):
                i+=1
            else:
                if(share_factor(i,seq[len(seq)-1])==True):
                    seq.append(i)
                    i=1
                    break
                else:
                    i+=1
    return seq.index(n)
​
​
def share_factor(n1,n2):
    for i in range(2,max(n1,n2)):
        if(n1%i==0 and n2%i==0):
            return True
    return False

