
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
​
def binary_to_decimal(str_x):
    return sum(int(str_x[-i]) * 2 ** (i - 1) for i in range(1, len(str_x) + 1))
​
​
def binary_to_fraction(str_x):
    numerator = binary_to_decimal(str_x)
    denominator = 2 ** len(str_x)
    return numerator, denominator
​
​
def binary_sum(lst):
    nums = []
    max_denominator = 1
    for x in lst:
        whole, fraction = x.split('.')
        whole = binary_to_decimal(whole)
        fraction = binary_to_fraction(fraction)
        if fraction[1] > max_denominator:
            max_denominator = fraction[1]
        nums.append([whole, fraction])
    whole_sum, numerator_sum = 0, 0
    for n in nums:
        whole_sum += n[0]
        numerator_sum += int(n[1][0] * max_denominator / n[1][1])
    whole_sum += numerator_sum // max_denominator
    numerator_remainder = numerator_sum % max_denominator
    if numerator_remainder:
        gcd_num_den = gcd(numerator_remainder, max_denominator)
        if whole_sum:
            return '{} {}/{}'.format(whole_sum,
                                     numerator_remainder // gcd_num_den,
                                     max_denominator // gcd_num_den)
        else:
            return '{}/{}'.format(numerator_remainder // gcd_num_den,
                                  max_denominator // gcd_num_den)
    else:
        return str(whole_sum)

