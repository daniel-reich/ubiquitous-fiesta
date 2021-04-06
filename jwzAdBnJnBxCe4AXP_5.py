
def rearranged_difference(num):
    return int("".join(sorted(str(num), reverse = True, key=max))) - int("".join(sorted(str(num), key=max)))

