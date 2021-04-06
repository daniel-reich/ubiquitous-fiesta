
def asteroid_collision(asteroids):
    left = []
    while len(asteroids) > 0 and asteroids[0] < 0:
        left.append(asteroids.pop(0))
    change = True
    while change and len(asteroids) >= 2:
        change = False
        for i in range(len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                # collision
                change = True
                if asteroids[i] == -asteroids[i+1]:
                    # both will be destroyed:
                    asteroids.pop(i)
                    asteroids.pop(i)
                elif asteroids[i] < -asteroids[i+1]:
                    asteroids.pop(i)
                else:
                    asteroids.pop(i+1)
                break
        while len(asteroids) > 0 and asteroids[0] < 0:
            left.append(asteroids.pop(0))
    ans = left + asteroids
    return ans

