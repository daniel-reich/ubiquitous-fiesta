
def worm_length(hyphens):
    if hyphens == "":
        return "invalid"
    for character in hyphens:
        if character != "-":
            return "invalid"
    length = len(hyphens)
    return str(length * 10) + " mm."

