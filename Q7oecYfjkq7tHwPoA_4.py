
def climb(stamina, obstacles):
    idx = 0
    while stamina > 0:
        if idx < len(obstacles) - 1:
            obstacle_diff = obstacles[idx + 1] - obstacles[idx]
            if obstacle_diff >= 0:
                stamina_loss = int(obstacle_diff) + int(obstacle_diff
                                                        > int(obstacle_diff))
                if stamina_loss * 2 <= stamina:
                    stamina -= stamina_loss * 2
                else:
                    return idx
            else:
                obstacle_diff *= -1
                stamina_loss = int(obstacle_diff) + int(obstacle_diff
                                                        > int(obstacle_diff))
                if stamina_loss <= stamina:
                    stamina -= stamina_loss
                else:
                    return idx
        else:
            return idx
        idx += 1
    return idx

