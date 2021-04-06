
def even_or_odd(s):
    even = sum([int(i) for i in s if int(i) % 2 == 0])
    odd = sum([int(i) for i in s if int(i) % 2 != 0])
    if even > odd:
        return "Even is greater than Odd"
    elif even < odd:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"

