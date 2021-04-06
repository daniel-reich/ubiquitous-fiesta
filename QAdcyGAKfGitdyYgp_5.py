
def bacteria(final_mass):
    day = 1
    last = [[1, 1.], [2, .5]]        # number of bacteria, mass per bacteria
    while True:
        # nightly mass increase:
        for k in range(len(last)):
            last[k][1] += 1.
            if last[k][0] * last[k][1] >= final_mass:
                return day
        # daily split/no split:
        day += 1
        cur = []
        for (n, mass) in last:
            if n * mass >= final_mass:
                return day
            # no split:
            cur.append([n, mass])
            # split:
            n_new = 2 * n
            mass_new = mass / 2.0
            total_mass = n_new * mass_new
            if total_mass >= final_mass:
                return day
            cur.append([n_new, mass_new])
        last = cur[:]

