
def binary_clock(time):
    time, bl = time.replace(':',''), []
    for x in range(6): bl.append("{0:b}".format(int(time[x])).zfill(4))
    return [" " +       bl[1][0] +  " " +      bl[3][0] +   " " +         bl[5][0],
            " " +       bl[1][1] +  bl[2][1] + bl[3][1] +   bl[4][1] +    bl[5][1],
            bl[0][2] +  bl[1][2] +  bl[2][2] + bl[3][2] +   bl[4][2] +    bl[5][2],
            bl[0][3] +  bl[1][3]+   bl[2][3] + bl[3][3] +   bl[4][3] +    bl[5][3]]

