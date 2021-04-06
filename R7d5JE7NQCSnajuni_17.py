
def convert_to_number(d):
    for k, v in d.items():
        d[k] = int(d[k])
    return d

