
def digits_of_num(n):
    digits = []
    count = 0
    temp = n
    while(temp > 0):
        count = count + 1
        digits.append(temp%10)
        temp = int(temp/10)
    digits.sort()
    
    return digits
​
import itertools
def permutations(digits):
    
    permutations_list = list(itertools.permutations([1,2,3]))
    
    return permutations_list
​
import math
import math
def is_vampire(n):
    if n < 100:
        return "Normal Number"
    # "Pseudovampire", "True Vampire"
    digits = digits_of_num(n)
    count = len(digits)
    
    permutations_list = list(itertools.permutations(digits))
    if count%2 == 0:
        count_half = int(count/2)
        
        for item in permutations_list:
            left  = 0
            right = 0
            for i in range(count_half):
                left  = left*10 + item[i]
                right = right*10 + item[count_half + i]
            
            if left*right == n:
                return "True Vampire"
    else:
        count_half = int((count-1)/2)
        for item in permutations_list:
            left  = 0
            right = 0
            for i in range(count_half):
                left  = left*10 + item[i]
                right = right*10 + item[count_half + i]
            right = right*10 + item[-1]
​
            if left*right == n:
                return "Pseudovampire"
    return "Normal Number"

