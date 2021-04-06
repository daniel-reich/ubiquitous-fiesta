
def base_conv(n, b):
    def base_10_to_base_b(n, b):
        w = 1
        while True:
            if n // (b ** w) == 0:
                break
            else:
                w += 1
        if w == 1:
            return chr(n % b + 97)
        o = []
        for ix in range(0, w):
            o[0:0] = chr(n % (b ** (ix + 1)) // (b ** ix) + 97)
            n -= n % (b ** (ix + 1))
        return ''.join(o)
​
    def base_b_to_base_10(n, b):
​
        is_not_alpha = [True if not ele.isalpha() else False for ele in n]
        is_out_of_range = [True if ord(ele) - ord('a') >= b else False for ele in n]
        if any(is_not_alpha) or any(is_out_of_range):
            return n + ' is not a base ' + str(b) + ' number.'
        d = [ord(ele) - ord('a') for ele in n]
        p = [b ** ix for ix in range(len(n) - 1, -1, -1)]
        s = [d[ix] * p[ix] for ix in range(len(d))]
        return sum(s)
​
    if type(n) is int:
        return base_10_to_base_b(n, b)
    else:
        return base_b_to_base_10(n, b)

