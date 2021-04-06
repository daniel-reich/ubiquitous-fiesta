
def sum_missing_numbers(lst):
    summa = 0
    maximum = max(lst)+1
​
    minimum = min(lst)
​
    for i in range(minimum, maximum):        
        summa += i
    print(summa)
    for item in lst:
        summa -= item
    
    return summa

