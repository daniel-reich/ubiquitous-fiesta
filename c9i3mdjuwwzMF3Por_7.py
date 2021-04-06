
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if not n % k:
            return False
    return True
​
​
def is_flippable(n):
    return all(c in '01689' for c in str(n))
​
​
def flip_num(n):
    return int(''.join({'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}[c]
                       for c in str(n)))
​
​
def bemirp(n):
    if str(n) != str(n)[::-1] and is_prime(n) and is_prime(int(str(n)[::-1])):
        if is_flippable(n):
            flipped_n = flip_num(n)
            if is_prime(flipped_n) and is_prime(int(str(flipped_n)[::-1])):
                return 'B'
        return 'E'
    elif is_prime(n):
        return 'P'
    else:
        return 'C'

