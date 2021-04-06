
def final(r, c, i):
    mat = [[0] * c for m in range(r)]
​
    for ele in i:
        index = int(ele[:len(ele)-1])
        if ele[-1] == 'r':
            for n in range(c):
                mat[index][n] += 1
        elif ele[-1] == 'c':
            for m in range(r):
                mat[m][index] += 1
    return mat
​
​
if __name__ == '__main__':
    mat = final(3, 3, ["2r", "2c", "1r", "0c"])
    print(mat)

