
def double_factorial(num): 
​
        if num == -1 or num == 0: 
            return 1
        
​
        if num % 2 == 0: 
            return num * double_factorial(num - 2)
        
        return num * double_factorial(num - 2)

