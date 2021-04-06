
def asteroid_collision(asteroids):
    i = 0
    while i < len(asteroids):
        if asteroids[i] > 0:
            if i + 1 < len(asteroids) and asteroids[i+1] < 0:
                s = asteroids[i] + asteroids[i+1]
                if s > 0: 
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i)
                    if s == 0: 
                        asteroids.pop(i)
                    i -= 1
                if i >= 0: continue
        i += 1
    return asteroids

