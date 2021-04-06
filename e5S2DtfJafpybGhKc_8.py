
def rotate(mat):
    res =[]
    temp=[]
    for v in range(len(mat[0])):
        for l in mat:
          temp.append(l[v])
        res.append(temp[::-1])
        temp=[]
    return res

