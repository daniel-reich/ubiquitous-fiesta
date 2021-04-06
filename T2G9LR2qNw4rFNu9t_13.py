
def chunk(array, size):
    rs =[]
    for i in range(0,len(array),size):
        rs.append(array[i:i+size])
    return rs

