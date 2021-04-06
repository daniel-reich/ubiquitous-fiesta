
def base_convert(num, base_num):
    if num < base_num:
        return [num]
    i = 0
    while base_num ** i < num:
        i += 1
    if num == base_num ** i:
        base_digit = i
        result = [0 for _ in range(i+1)]
    else:
        base_digit = i -1
        result = [0 for _ in range(i)]
    for k in range(i):
        if (num // base_num ** base_digit) == 0:
            result[k] = 0
        elif num // base_num ** (base_digit) > 0 and num % base_num ** (base_digit) == 0:
           result[k] = (num // base_num ** (base_digit))
        elif num // base_num ** (base_digit) > 0 and num % base_num ** (base_digit) != 0:
           result[k] = (num // base_num ** (base_digit))
        num -= (num // base_num ** (base_digit)) * (base_num ** (base_digit))
        base_digit -= 1
    return result
​
def base_n(base, values, num):
    if len(values) != base:
        return False
    result_base = base_convert(num, base)
    result = ""
    for num in result_base:
        result += str(values[num])
    return result

