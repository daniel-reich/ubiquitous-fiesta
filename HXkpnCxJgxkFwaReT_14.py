
def count_datatypes(*args):
​
    type_count = [0, 0, 0, 0, 0, 0]
​
    for arg in args:
        if isinstance(arg, bool):
            type_count[2] = type_count[2] + 1
            continue
        elif isinstance(arg, int):
            type_count[0] = type_count[0] + 1
            continue
        elif isinstance(arg, str):
            type_count[1] = type_count[1] + 1
            continue
        elif isinstance(arg, list):
            type_count[3] = type_count[3] + 1
            continue
        elif isinstance(arg, tuple):
            type_count[4] = type_count[4] + 1
            continue
        elif isinstance(arg, dict):
            type_count[5] = type_count[5] + 1
            continue
​
    return type_count

