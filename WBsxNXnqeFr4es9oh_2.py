
def clockwise_cipher(message):
    size = 1
    while size**2 < len(message):
        size += 1
    grid = [[' ' for _ in range(size)] for __ in range(size)]
    cur_size = size
    offset = 0
    idx = 0
    while idx < len(message) and cur_size > 1:
        for k in range(cur_size-1):
            grid[offset][offset+k] = message[idx]
            idx += 1
            if idx >= len(message): break
            if k < cur_size - 1:
                grid[offset+k][size-1-offset] = message[idx]
                idx += 1
                if idx >= len(message): break
            grid[size-1-offset][size-1-offset-k] = message[idx]
            idx += 1
            if idx >= len(message): break
            if k < cur_size - 1:
                grid[size-1-offset-k][offset] = message[idx]
                idx += 1
                if idx >= len(message): break
        offset += 1
        cur_size -= 2
    if len(message) == size**2:
        grid[size//2][size//2] = message[-1]
    ans = ""
    for row in grid:
        #print(''.join(row))
        ans += ''.join(row)
    return ans

