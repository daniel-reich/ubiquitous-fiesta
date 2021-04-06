
def factors(num):
    counter = 2
    for val in range(2, num//2 + 1):
        if num%val == 0: 
            counter += 1
    return counter
    
def factor_sort(lst):
    factor_lst = sorted(list(zip(lst, [factors(num) for num in lst])), key=lambda elm: (elm[1], elm[0]), reverse=True)
    return [elm[0] for elm in factor_lst]

