
def create_square(length):
    if not length:
        return ""
    return "\n".join("#"*length if ch == 0 or ch == length - 1 else "#{}#".format(" "*(length-2)) for ch in range(length))

