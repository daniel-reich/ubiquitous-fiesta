
def smith_type(number):
    if smith(number) == True:
        if smith(number+1) == True:
            return("Youngest Smith")
        elif smith(number-1) == True:
            return("Oldest Smith")
        else:
            return("Single Smith")
    elif smith(number) == "Trivial Smith":
        return("Trivial Smith")
    else:
        return("Not a Smith")
    
def smith(number):
    dr_num = 9 if number%9 == 0 else number%9
    prime_nums = []
    for i in range(2, number):
        if [j for j in range(2, i) if i%j==0] == []:
            prime_nums.append(i)
    prime_factors = []
    a = number
    for x in prime_nums:
        while a%x == 0 and a > 1:
            prime_factors.append(x)
            a = a/x
    if prime_factors == [] and number != 1:
        smith = "Trivial Smith"
    elif number == 1:
        smith = "Not a Smith"
    else:
        # dr_spf refers to digit root of the sum of prime factors
        dr_spf = 9 if sum(prime_factors)%9 == 0 else sum(prime_factors)%9 
        smith = (dr_num == dr_spf)
    return(smith)

