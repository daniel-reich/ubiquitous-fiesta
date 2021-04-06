
def prime_factorization(number):
    temp = []
    while number % 2 == 0: 
        temp.append(2) 
        number = number // 2
          
    for i in range(3,int(number**.5)+1,2):      
        while number % i== 0: 
            temp.append(i)
            number = number // i 
              
    if number > 2: 
        temp.append(number)
    return temp

