
def complete_bracelet(lst):
    for length in range(2, len(lst)//2 + 1):
        count = 1
        for start in range(0, len(lst)-length + 1):
            if lst[start:start+length] == lst[start + length:start + (2 * length) ]:
                count += 1
                if count * length == len(lst):
                    return True
                else:
                    continue
    return False

