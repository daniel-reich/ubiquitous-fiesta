
def is_prime(n):
    return True if n == 2 else False if n == 1 else all(n % num != 0 for num in range(2, n))
​
def all_prime(nums):
    return all(is_prime(x) for x in nums)

