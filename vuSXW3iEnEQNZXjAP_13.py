
def create_square(length):
    r = []
    if length == None or length < 1:
        return ""
    for i in range(length):
        if i == 0 or i == length - 1:
            r.append("#" * length)
        else:
            r.append("#" + " " * (length - 2) + "#")
    return "\n".join(r)

