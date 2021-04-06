
def digit_distance(num1, num2):
​
    length = len(str(num1)) # Both digits are same length
    
    numbers_to_sum = []
    
    for d in range(0, length):
        
        dig_dist = abs(int(str(num1)[d]) - int(str(num2)[d]))
        
        numbers_to_sum.append(dig_dist)
        
    return(sum(numbers_to_sum))

