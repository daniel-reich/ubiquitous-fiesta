
def lets_meet(dist, v1, v2):
    t = 1000 * dist / ((v1 + v2) * 1000 / 3600)
    return "{0}h {1}min {2}s".format(int(t // 3600), int(t % 3600 // 60), int(t % 3600 % 60))

