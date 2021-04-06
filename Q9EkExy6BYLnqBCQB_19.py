
def wrap_around(string, offset):
    _, offset = divmod(offset, len(string))
    return string[offset:] + string[: offset]

