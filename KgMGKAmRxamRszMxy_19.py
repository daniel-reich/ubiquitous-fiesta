
def spartans_cipher(msg, n_slide):
    length = len(msg)
    cipher = ''
    while length % n_slide != 0:
        msg += ' '
        length += 1
    columns = length//n_slide
    for x in range(columns):
        for y in range(x, length, columns):
            cipher += msg[y]
    return cipher.rstrip()

