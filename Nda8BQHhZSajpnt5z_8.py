
def GCD(lst):
    def divisor(number):
        divisor_list = []
        for i in range(1,number+1):
            if number%i == 0:
                divisor_list.append(i)
        return divisor_list
​
    def intersect(lst1,lst2):
        intersect = []
        for l1 in lst1:
            if l1 in lst2:
                intersect.append(l1)
        return intersect
​
    common_divisor = []
    for l in lst:
        common_divisor.append(divisor(l))
    for i in range(len(lst)-1):
        common_divisor[i+1] = intersect(common_divisor[i],common_divisor[i+1])
    return max(common_divisor[-1])

