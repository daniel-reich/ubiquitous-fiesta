
def freq_count(lst, el):
    counter = {0: 0}
    for item in lst:
        if isinstance(item, list):
            for key, val in freq_count(item, el):
                counter[key + 1] = counter.get(key + 1, 0) + val
        elif item == el:
            counter[0] += 1
    return [[k, v] for k, v in counter.items()]

