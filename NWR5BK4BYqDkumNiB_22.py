
def digital_division(n):
    vals_to_consider=([int(val) for val in str(n)])
    ti=0
    while ti==0:
        try:
            vals_to_consider.remove(0)
        except:
            ti=1
    check_1=0
    tests=0
    t3_val=1
    for vvals in vals_to_consider:
    #test 1 - Exactly divisble be each of its digits excluding 0
        if n%vvals == 0:
            check_1=check_1+1
            
        if check_1 == len(vals_to_consider):
            tests=tests+1
    
​
    #test 2 exactly divisible by sum of digits
    if n%sum(vals_to_consider)  == 0:
        tests=tests+1
    #test3 exactly divisible by product on digits
    for vvals in [int(val) for val in str(n)]:    
        t3_val=t3_val*vvals
    try:
        n%t3_val==0
        if n%t3_val==0:
            tests=tests+1
    except:
        tests=tests
    if tests == 3:
        return("Perfect")
    elif tests > 0:
        return(tests)
    else:
         return("Indivisible")

