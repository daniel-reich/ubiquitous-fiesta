
def factor_sort(nums):
    def factor_length(n):
        if n == 1:
            return 1
        return sum(x for x in range(2, n // 2 + 1) if n % x == 0) + 2
​
    return sorted(sorted(nums, reverse=True), key=factor_length, reverse=True)

