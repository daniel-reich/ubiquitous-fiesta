
def base_convert(num, base_num):
    if num < base_num:
        return [num]
    i = 0
    while base_num ** i < num:
        i += 1
    if num == base_num ** i:
        base_digit = i
        result = [0 for _ in range(i + 1)]
    else:
        base_digit = i - 1
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
def base_conv(n, b):
    if type(n) == int:
       result_base = base_convert(n, b)
       result = ""
       for num in result_base:
           result += chr(num + ord("a"))
    elif type(n) == str:
        result = 0
        for i in range(len(n)):
            if 0 <= (ord(n[i]) - ord("a")) < b:
                result += (ord(n[i]) - ord("a")) * (b ** (len(n) - i -1))
            else:
                return "{} is not a base {} number.".format(n, b)
​
    return result

