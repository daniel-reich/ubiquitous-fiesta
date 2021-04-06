
import itertools
​
def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
def ruth_aaron(n):
    pfn1 = list(factors(n))
    pfn2 = list(factors(n-1))
    pfn3 = list(factors(n+1))
    sum1 = sum(pfn1)
    sum2 = sum(pfn2)
    sum3 = sum(pfn3)
    sum1_dist = sum(list(set(pfn1)))
    sum2_dist = sum(list(set(pfn2)))
    sum3_dist = sum(list(set(pfn3)))
    if sum1 == sum2 and sum1_dist == sum2_dist:
        return ['Aaron',3]
    if sum1 == sum3 and sum1_dist == sum3_dist:
        return ['Ruth',3]
    if sum1 == sum2:
        return ['Aaron',2]
    if sum1 == sum3:
        return ['Ruth',2]
    if sum1_dist == sum2_dist:
        return ['Aaron',1]
    if sum1_dist == sum3_dist:
        return ['Ruth',1]
    return False

