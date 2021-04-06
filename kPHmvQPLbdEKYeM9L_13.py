
def asteroid_collision(asteroids):
    if asteroids == []:
        return []
    result_lst = [asteroids[0]]
    for i in range(1, len(asteroids)):
        if asteroids[i] < 0 and asteroids[i - 1] < 0:
            result_lst.append(asteroids[i])
        elif asteroids[i] > 0 and asteroids[i - 1] > 0:
            result_lst.append(asteroids[i])
        elif asteroids[i-1] < 0 and asteroids[i] > 0:
            result_lst.append(asteroids[i])
        elif asteroids[i-1] > 0 and asteroids[i] < 0:
            if abs(asteroids[i]) > asteroids[i-1]:
                result_lst.pop()
                result_lst.append(asteroids[i])
            elif abs(asteroids[i]) == asteroids[i - 1]:
                result_lst.pop()
    if result_lst == [] or result_lst == asteroids:
        return result_lst
    return asteroid_collision(result_lst)

