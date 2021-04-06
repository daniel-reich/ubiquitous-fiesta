
def asteroid_collision(asteroids):
    n = len(asteroids)
    if n < 2:
        return asteroids
    crashed = {i: False for i in range(n)}
    current = other = 1 if asteroids[0] < 0 else 0
    while current < n:
        direction = asteroids[current] > 0
        other += 1 if direction else -1
        if other >= n:
            break
        elif other < 0:
            current += 1
            other = current
            continue
​
        other_direction = asteroids[other] > 0
​
        if crashed[current]:
            current += 1
            other = current
        elif other_direction == direction and other_direction:
            current = other
        elif other_direction != direction:
            if not crashed[other]:
                mass = abs(asteroids[current])
                other_mass = abs(asteroids[other])
                if mass > other_mass:
                    crashed[other] = True
                elif mass < other_mass:
                    crashed[current] = True
                    current += 1
                    other = current
                else:
                    crashed[current] = True
                    crashed[other] = True
                    current += 1
                    other = current
            elif direction:
                current += 1
                other = current
    return [asteroids[i] for i in range(n) if not crashed[i]]

