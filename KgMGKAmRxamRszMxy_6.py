
def spartans_cipher(message, n_Slide):
    n = len(message)
    cols = n // n_Slide
    if n % n_Slide != 0:
        cols += 1
    grid = []
    for k in range(n_Slide):
        grid.append([_ for _ in message[k*cols:k*cols+cols]])
    for r in range(n_Slide):
        while len(grid[r]) < cols:
            grid[r].append(' ')
    cipher = ""
    for col in range(cols):
        cipher += ''.join([grid[r][col] for r in range(n_Slide)])
    return cipher.strip()

