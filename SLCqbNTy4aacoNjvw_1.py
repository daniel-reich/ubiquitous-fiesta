
def remove_dups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

