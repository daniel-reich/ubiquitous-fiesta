
def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        return 'invalid'
    ans = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            temp2 = []
            for k in range(len(b)):
                temp2.append(a[i][k] * b[k][j])
            temp.append(sum(temp2))
        ans.append(temp)
    return ans

