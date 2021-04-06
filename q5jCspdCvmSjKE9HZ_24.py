
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
​
def lcm_of_list(numbers):
    solution = 1
    for i in numbers:
        solution = solution*i//gcd(solution, i)
    return solution

