
from itertools import permutations as perm
def is_vampire(n):
    if n>99:
        a=len(str(n))//2
        p=perm(str(n))
        for i in p:
            n1=''.join(i)
            if len(str(n))%2==1:
                if int(n1[:a+1])*int(n1[a+1:])==n or int(n1[:a])*int(n1[a:])==n:
                    return 'Pseudovampire'
            else:
                if int(n1[:a])*int(n1[a:])==n:
                   
                    return 'True Vampire'
    return 'Normal Number'
​
print(is_vampire(1260))

