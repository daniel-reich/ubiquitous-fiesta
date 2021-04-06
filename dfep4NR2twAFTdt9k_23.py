
def matrix_mult(m1,m2):
    ans= [[0,0],[0,0]]
    for i in range(2):
       for j in range(2):
           for k in range(2):
               ans[i][j] += m1[i][k] * m2[k][j]
    return ans

