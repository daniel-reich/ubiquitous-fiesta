
def asteroid_collision(asteroids):
    sol = []
    for num in asteroids:
        while sol and sol[-1] > 0 and sol[-1] + num < 0:
            sol.pop()
        if not sol or sol[-1] < 0 or num > 0:
            sol.append(num)
        elif num < 0 and sol[-1] + num == 0:
            sol.pop()
    return sol

