
def hex_lattice(n):
    if n == 1:
        return " o "
    hex_len = 1 + (-1 + (1 + 4 * ((n - 1) / 3)) ** 0.5) / 2
    if int(hex_len) != hex_len:
        return "Invalid"
    out = ""
    hex_len = int(hex_len)
    for k in range(hex_len-1):
        out += " "*(hex_len - k) + "o "*(hex_len + k) + " "*(hex_len - k -1)
        if k < hex_len-2:
            out += "\n"
    return out + "\n " + "o "*(2*hex_len - 1) + "\n" + out[::-1]

