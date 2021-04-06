
def asteroid_collision(asteroids):
        res = []
        stack = [] 
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                killed = False
                while len(stack) > 0:
                    last = stack[-1]
                    if abs(asteroid) >= last:
                        stack.pop(-1)
                        if abs(asteroid) == last:
                            killed = True
                            break                        
                    else:
                        break
                if not killed and len(stack) == 0:
                    res.append(asteroid)
        return res + stack

