
def calculate_sum(nums):
    return sum(x for x in nums)
​
​
def is_prob_matrix(arr):
    return all(len(n) == len(arr) and int(calculate_sum(n)) == 1 and min(n) >= 0 and max(n) <= 1.0 for n in arr)

