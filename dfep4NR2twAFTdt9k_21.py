
def matrix_mult(m1, m2):
​
    matrix = ['','']
    
    matrix[0] =[[m1[0][0],m2[0][0]],[m1[0][1],m2[1][0]],[m1[0][0],m2[0][1]],[m1[0][1],m2[1][1]]]
​
    matrix[1] = [[m1[1][0],m2[0][0]],[m1[1][1],m2[1][0]],[m1[1][0],m2[0][1]],[m1[1][1],m2[1][1]]]
​
    lis = []
​
    for i in matrix:
        l1 = i[0][0] * i[0][1]
        l2 = i[1][0] * i[1][1]
​
        l3 = i[2][0] * i[2][1]
        l4 = i[3][0] * i[3][1]
​
        ans1 = l1 + l2
        ans2 = l3 + l4
​
        lis.append([ans1,ans2])
    
    return lis

