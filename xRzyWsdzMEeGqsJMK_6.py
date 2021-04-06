
def maskify(string):
    if len(string) <= 4:
        return string
    else:
        return "".join(["#" for char in range(len(string)-4)]) + string[-4:]

