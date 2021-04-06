
def is_untouchable(n):
    if n<2: return "Invalid Input"
    sum_divisors=lambda n: 1+sum([i if (i == (n/i)) else (i + n//i)  for i in [i for i in range(2,1+int(n**0.5)) if not n%i]])
    untouchable_list=[i for i in range(2,n**2) if sum_divisors(i)==n]
    return True if not untouchable_list else untouchable_list

