
def rail_fence_cipher(message, rails):
    road, r, step = [[] for _ in range(rails)], 0, 1
    for c in message:
        if r == 0:
            step = 1
        elif r == rails - 1:
            step = -1
        road[r].append(c)
        r += step
    return "".join("".join(road[r]) for r in range(rails))

