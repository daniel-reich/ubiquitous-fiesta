
ring_steps = [
    [0, 1, 2, 3, 4, -3, -2, -1],   
    [-1, 0, 1, 2, 3, 4, -3, -2],   
    [-2, -1, 0, 1, 2, 3, 4, -3],   
    [-3, -2, -1, 0, 1, 2, 3, 4],   
    [4, -3, -2, -1, 0, 1, 2, 3],   
    [3, 4, -3, -2, -1, 0, 1, 2],   
    [2, 3, 4, -3, -2, -1, 0, 1],
    [1, 2, 3, 4, -3, -2, -1, 0]
]
​
def spider_vs_fly(spider, fly):
    s0, s1 = "ABCDEFGH".index(spider[0]), int(spider[1])
    f0, f1 = "ABCDEFGH".index(fly[0]), int(fly[1])
    s2f_ring = ring_steps[s0][f0]
    s2f_radial = s1 - f1
    path = [spider]
    if abs(s2f_ring) > 2:
        # if angle between radii > 90 degrees always go via centre
        for i in range(s1-1, 0, -1):
            path.append(spider[0] + str(i))
        path.append("A0")
        s1 = 0
    else:
        if s2f_radial > 0:
            # if fly closer to centre move radially to same ring
            for i in range(s1-1, f1-1, -1):
                path.append(spider[0] + str(i))
                s1 = i
        # move along ring to fly's ring
        dirn = 1 if s2f_ring >= 0 else -1
        radial = s0
        while radial != f0:
            radial += dirn
            if radial < 0:
                radial += 8
            path.append("ABCDEFGH"[radial] + str(s1))
    # finally move radially to fly's ring and gobble
    for i in range(s1+1, f1+1):
        path.append(fly[0] + str(i))
    return "-".join(path)

