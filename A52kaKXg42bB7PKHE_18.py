
def num_then_char(lst):
    lengths = list(map(len, lst))
    numbers = sorted([num for sublst in lst for num in sublst if type(num) in [int, float]])
    chars = sorted([c for sublst in lst for c in sublst if type(c) == str])
    all = numbers + chars
    res = []
    slice_start = 0
    slice_end = lengths[0]
    for i in range(1, len(lengths)):
        res.append(all[slice_start:slice_end])
        slice_start = slice_end
        slice_end = slice_start + lengths[i]
        # print("start=",slice_start,"end=", slice_end,"i=",lengths[i])
    res.append(all[slice_start:slice_end])
    return res

