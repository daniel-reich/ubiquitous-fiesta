
def sum_odd_and_even(lst):
    even = sum([i for i in lst if i%2==0])
    odd = sum([i for i in lst if i%2!=0])
    return [even, odd]

