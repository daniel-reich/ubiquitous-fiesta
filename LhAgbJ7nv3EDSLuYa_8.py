
def golomb(n):
    myseq = [1,2,2,3,3]
​
    for i in range(3,n):
        for j in range(myseq[i]):
            myseq.append(i+1)
​
    return myseq[:n]

