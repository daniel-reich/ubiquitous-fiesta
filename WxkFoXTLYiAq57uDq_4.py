
def find_and_remove(d):
    cleaned = {}
    for room in d:
        cleaned[room] = {k: int(v) for k, v in d[room].items() if v.isdigit()}
    return cleaned

