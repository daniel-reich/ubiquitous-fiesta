
def recaman(n):
    out_format = "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}"
    sequence, unique_values, duplicates, duplicate_set = [], set(), [], set()
    for i in range(n):
        if i == 0:
            an = 0
        else:
            an = sequence[-1] - i
            if an <= 0 or an in unique_values:
                an = sequence[-1] + i
        if an in unique_values and not an in duplicate_set:
            duplicates.append(an)
            duplicate_set.add(an)
        unique_values.add(an)
        sequence.append(an)
    return out_format.format(sequence, n, duplicates)

