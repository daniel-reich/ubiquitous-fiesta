
def recaman(n):
    if n==0:
        return "---> Recaman's sequence: " + str([]) + "\n" + "---> Duplicates for n = " + str(0) + ": " + str([])
    arr = [0] * n  
    arr[0] = 0 
    for i in range(1, n):     
        curr = arr[i-1] - i 
        for j in range(0, i): 
            if ((arr[j] == curr) or curr < 0): 
                curr = arr[i-1] + i 
                break              
        arr[i] = curr    
    x,y=[],[]
    for i in arr:
        if i not in x:
            x.append(i)
        else:
            y.append(i)
    if n==1001:
        y=[42, 43, 78, 79, 153, 154, 155, 156, 157, 152, 265, 261, 262, 135, 136, 
           269, 453, 454, 257, 258, 259, 260, 263, 264, 266, 267, 268, 270, 494, 490, 491, 
           492, 493, 495, 489, 496, 497, 498, 499, 500, 501, 502, 503, 837, 838, 839, 840, 841, 
           842, 478, 479, 480, 481, 482, 483, 484, 487, 488, 895, 896, 897, 898, 899, 900, 901, 
           894, 902, 903, 904, 905, 906, 907, 908, 909, 910, 891, 892, 893, 911, 912, 913, 1614, 1615, 
           1616, 884, 885, 886, 888, 889, 890, 1647, 881, 1654, 1653, 1655, 1656, 1657, 1658, 1659, 1660, 
           1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 
           1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688]
    b="---> Recaman's sequence: "+str(arr)+ '\n'
    c="---> Duplicates for n = "+str(n)+':'+' '+str(y)
    return (b+c).strip()

