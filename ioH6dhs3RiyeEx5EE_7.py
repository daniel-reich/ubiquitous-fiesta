
def make_fun_lst(n1, n2):
    def f2(num):
        def wrapper(x):
            return x*num
        return wrapper
    def f1(num):
        def wrapper(x):
            return x + num
        return wrapper
​
    result = []
​
    
    for number in range(n1, n2):        
               
        if number%2 == 0:
            
            a = f1(number)      
            result.append(a)
        else:
            
            b = f2(number)  
            result.append(b)
    return result

