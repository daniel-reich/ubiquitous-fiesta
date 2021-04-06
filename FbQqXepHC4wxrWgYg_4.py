
def prime_divisors(num):
    a = [1]
    b = [1]
    final_list = []
    f = 2
    f2 = 2
    while num>1:
        if num%f==0:
            a.append(f)
            
            f+=1
        else:
            f+=1
        if f>num+1:
            break
    #print'all divisors of {} = '.format(num) , a
​
    for i in a:
        b = [1]
        f2 = 2
        while i>1:
            if i%f2==0:
                b.append(f2)
            
                f2+=1
            else:
                f2+=1
            if f2>i+1:
                break
        #print b,'for {}'.format(i)
​
        if len(b)<3:
           # print "True for {}" . format(i)
            final_list.append(i)
        #else:print "False for {}".format(i)
    return final_list

