
def fire(matrix, coordinates):
    dic ={"A":0, "B":1, "C":2, "D":3, "E":4}
    l,n = coordinates
    return "BOOM" if matrix[dic[l]][int(n)-1]=="*" else "splash"

