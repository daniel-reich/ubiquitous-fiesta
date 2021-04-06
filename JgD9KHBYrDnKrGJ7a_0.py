
def swap_dict(dic):
    result = {}
    for key, value in dic.items():
        result.setdefault(value, []).append(key)
    return result

