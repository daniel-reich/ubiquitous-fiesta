
def matrix_mult(m1, m2):
    myans = [[1,2],[3,4]]
​
    myans[0][0] = m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0] 
    myans[0][1] = m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]
    myans[1][0] = m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0]
    myans[1][1] = m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]
    
    return myans

