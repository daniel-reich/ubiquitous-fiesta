
def primes(n):
    if n<2:return False
    if n==2:return True
    return all([n%c!=0 for c in range(2,int(n**(1/2))+2)])
def product_of_primes(num):
    i=2
    lst=[]
    while num>1:
        if num%i==0:
            lst.append(i)
            num/=i
        if primes(num):
            lst.append(int(num))
            break
        if num%i!=0:i+=1
    return set(lst)
def ecg_seq_index(n):
    all_list=[1,2]
    for _ in range(n*2):
        not_in_list=[]
        for i in product_of_primes(all_list[-1]):
            if i not in all_list:
                not_in_list.append(i)
                break
            org_i=i
            while i in all_list:
                i+=org_i    
                if i not in all_list:
                    not_in_list.append(i)
                    break
        all_list.append(min(not_in_list))
    return all_list.index(n)

