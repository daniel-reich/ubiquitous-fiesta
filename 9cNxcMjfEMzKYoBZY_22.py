
def num_type(number):
    
    divisor_sum = calculate_divisor(number)
    
    if divisor_sum == number:
        return "Perfect"
    
    if divisor_sum != number:
        divisor_sum2 = calculate_divisor(divisor_sum)
        if divisor_sum2 == number:
            return "Amicable"
        else:
            return "Neither"
​
def calculate_divisor(listing):
    positive_divisor = []
    for num in range(1,listing):
        if listing % num == 0:
            positive_divisor.append(num)
    return sum(positive_divisor)

