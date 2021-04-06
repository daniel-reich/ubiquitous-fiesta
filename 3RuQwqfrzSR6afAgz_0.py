
def rail_fence_cipher(message, rails):
    rows = [""] * rails
    rows[0] += message[0]
    idx = 1
    n = len(message)
    while idx < n:
        for row in range(1, rails):
            rows[row] += message[idx]
            idx += 1
            if idx == n:
                break
        for row in range(rails - 2, -1, -1):
            if idx == n:
                break
            rows[row] += message[idx]
            idx += 1
    return ''.join(rows)

