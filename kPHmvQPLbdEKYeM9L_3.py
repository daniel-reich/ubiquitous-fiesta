
def asteroid_collision(asteroids):
    i = 0
    while i + 1 < len(asteroids):
        a, b = asteroids[i], asteroids[i + 1]
        if a > 0 and b < 0:
            i = -1
            if a + b == 0:
                asteroids.remove(a)
                asteroids.remove(b)
            else:
                if abs(a) > abs(b):
                    asteroids.remove(b)
                else:
                    asteroids.remove(a)
        i += 1
    return asteroids

