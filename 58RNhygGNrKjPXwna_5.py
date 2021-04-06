
def longest_nonrepeating_substring(txt):
    position_hash, current_start, max_sub_length, max_sub_start = {}, 0, 0, 0
    for i in range(len(txt)):
        if txt[i] not in position_hash: position_hash[txt[i]] = i
        else:
            if position_hash[txt[i]] >= current_start:
                if max_sub_length < i - current_start: max_sub_length, max_sub_start = i - current_start, current_start
                current_start = position_hash[txt[i]] + 1
            position_hash[txt[i]] = i
    if max_sub_length < i + 1 - current_start: max_sub_length, max_sub_start = i + 1 - current_start, current_start
    return txt[max_sub_start: max_sub_start + max_sub_length]

