
def prime_numbers(num):
    def isprime(n):
        ret = [num for num in range(1, n + 1) if not n % num]
        return len(ret) == 2
​
    return sum([1 for i in range(1, num) if isprime(i)])

