
def int_to_vlq(n):
    if n == 0:
        return [0]
    byte = []
    while n > 0:
        value_bits = n & 0b1111111
        if len(byte) == 0:
            byte.append(value_bits)
        else:
            byte.append((0b1 << 7) | value_bits)
        n >>= 7
    return list(reversed(byte))
def vlq_to_int(lst):
    if lst[-1] >> 7 == 1:
        raise ValueError(
            "Incomplete sequence.  Last byte has continuation bit set.")
​
    result = []
    current_result = 0
    for byt in lst:
        current_result = (current_result << 7) | (byt & 0b1111111)
        if byt >> 7 == 0:
            result.append(current_result)
            current_result = 0
    return result[0]

