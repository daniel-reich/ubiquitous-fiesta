
def bitwise_index(lst):
    for i, v in enumerate(lst):
        if bin(v)[-1] == '0':
            idx, largest = i, v
            break
    else:
        return 'No even integer found!'
    for i, v in enumerate(lst):
        if bin(v)[-1] == '0' and v > largest:
            largest = v
            idx = i
    return {'@{} index {}'.format(['even', 'odd'][int(bin(idx)[-1])],
                                  idx): largest}

