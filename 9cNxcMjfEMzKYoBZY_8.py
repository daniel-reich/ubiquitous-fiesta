
def sum_of_posi_div(n):
    return sum([i for i in range(1, n) if not n % i])
​
​
def num_type(n):
    if sum_of_posi_div(n) == n:
        return 'Perfect'
    elif n == sum_of_posi_div(sum_of_posi_div(n)):
        return 'Amicable'
    else:
        return 'Neither'
​
​
print(num_type(6))
print(num_type(2924))
print(num_type(5010))

