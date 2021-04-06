
mini_peaks = lambda r: [y for x, y, z in zip(r, r[1:], r[2:]) if x < y and y > z]

