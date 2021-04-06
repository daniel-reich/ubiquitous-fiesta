
def concatenation_sum(n):
    """Thanks to @eleb formula"""
    len_n = len(str(n + 1))
    return (n + 1) * len_n - int('1' * len_n)

