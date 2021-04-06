
def prime_factors(num):
    my_list = []
    
    for i in range(2, int(num)):
        if num % i == 0:
            while num % i == 0:
                my_list.append(i)
                num /= i
    return my_list

