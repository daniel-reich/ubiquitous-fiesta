
def num_length(n):
    k = 0
    while n:
        k += 1
        n //= 10
    return k
​
def swap_digit(a, d, p):
    def helper(a, d, p, c, k):
        if p == 0:
            return (a // 10 * 10  + d) * k + c
        return helper(a // 10, d, p - 1, c + k * (a % 10), k * 10)
    return helper(a, d, p, 0, 1)
​
def maximizer(a, b):
    if not b:
        return a
    swap_combos = [a] + [swap_digit(a, b % 10, i) for i in range(0, num_length(a))]
    swap_combos = [maximizer(o, b // 10) for o in swap_combos]
    return max(swap_combos)
​
def max_possible(n1, n2):
  return maximizer(n1, n2)

