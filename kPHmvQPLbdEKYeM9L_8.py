
def asteroid_collision(asteroids):
        x = 0
        while x < len(asteroids) * 5:  # nah, efficiency bad
            for i in range(len(asteroids) - 1):
                as1 = asteroids[i];
                as2 = asteroids[i + 1]
                if as1 > 0 and as2 < 0:
                    if as1 > abs(as2):
                        asteroids.pop(i + 1)
                    elif as1 == abs(as2):
                        asteroids.pop(i)
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i)
                    break
            x += 1
        return asteroids

