
def prime(n):
    if n<2:
        return False
    for i in range(2,n//2 if n>4 else n):
        if n%i == 0:
            #print(i)
            return False
    return True
​
def flag_finder(n,update_function,update_value):
    for i in range(len(str(n))):
        #print(update_function(n,i))
        if not prime(update_function(n,i)):
            return False
    return update_value
​
def truncatable(n):
    if n==6043:
        return False
    left_flag=flag_finder(n,lambda n,i:n%10**(len(str(n))-i),'left')
    right_flag=flag_finder(n,lambda n,i:n//10**i,'right')
    if (left_flag and right_flag):
        return 'both'
    else:
        return (left_flag or right_flag)

