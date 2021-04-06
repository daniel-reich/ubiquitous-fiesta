
def is_anti_list(list_a: list, list_b: list):
    if len(set(list_a) | set(list_b)) == 2:
        for a, b in zip(list_a, list_b):
            if a == b:
                return False
        return True
    return False

