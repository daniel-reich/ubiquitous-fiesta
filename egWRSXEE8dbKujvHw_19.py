
def is_circle_collision(c1, c2):
    return (c2[1]-c1[1]) **2 + (c2[-1] - c1[-1])**2 <= (c1[0] ** 2 + c2[0] ** 2)

