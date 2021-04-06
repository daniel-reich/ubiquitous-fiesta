
c = []
for i in range(2,5000):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        c.append(i)
def cuban_prime(num):
    p = [1+3*y*(y+1) for y in range(1,100)]
    return '{} is cuban prime'.format(num) if num in set(c) & set(p) else '{} is not cuban prime'.format(num)

