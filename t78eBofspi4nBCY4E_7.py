
def base_conv(n, b):
    base_str = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    rest = []
    result = ''
​
    if isinstance(n, int):
​
        while n // b > 0:
            rest.append(n % b)
            n = n // b
        rest.append(n % b)
​
        for item in rest:
            result += base_str[item]
​
        return result[::-1]
​
    for letter in n:
        if letter not in base_str[:b]:
            return str(n) + ' is not a base ' + str(b) + ' number.'
​
    rest = [base_str.index(letter) for letter in n[::-1]]
    return sum([item * (b ** index) for index, item in enumerate(rest)])

