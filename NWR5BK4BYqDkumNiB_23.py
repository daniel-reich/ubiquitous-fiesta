
def divisible_by_each_digit(n):  
    number = n
​
    while number > 0:
        remainder = number % 10
        if remainder != 0:
            if n % remainder != 0:
                return False
        number = number // 10
    
    return True
​
​
def divisible_by_sum_of_digits(n):  
    total = 0
    number = n
​
    # getting sum of its digits
    while number > 0:
        total += number % 10
        number = number // 10
        
    if n % total == 0:
        return True
    
    return False
​
​
def divisible_by_product_of_digits(n):  
    product = 1
    number = n
​
    # getting product of its digits
    while number > 0:
        product = product * (number % 10)
        number = number // 10
​
    if product != 0:   
        if n % product == 0:
            return True
    
    return False
​
​
def digital_division(n):
    holder = []
​
    holder.append(divisible_by_each_digit(n))
    holder.append(divisible_by_sum_of_digits(n))
    holder.append(divisible_by_product_of_digits(n))
​
    if all(holder):
        return 'Perfect'
    if not any(holder):
        return 'Indivisible'
    
    return holder.count(True)

