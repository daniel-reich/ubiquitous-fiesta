
from collections import defaultdict
​
​
def is_economical(n):
    def is_prime(n):
        if n > 1:
            # check for factors
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        else:
            return False
​
    n_length = len(str(n))
    total = defaultdict(int)
    score = 0
    while True:
        for i in range(2, n+1):
            if is_prime(i) and n % i == 0:
                n = n // i
                total[i] += 1
                if is_prime(n) or n == 1:
                    if n > 1:
                        total[n] += 1
                    for k, v in total.items():
                        if v > 1:
                            score += len(str(k)) + len(str(v))
                        else:
                            score += len(str(k))
                    if score == n_length:
                        return 'Equidigital'
                    if score < n_length:
                        return 'Frugal'
                    return 'Wasteful'
                break

