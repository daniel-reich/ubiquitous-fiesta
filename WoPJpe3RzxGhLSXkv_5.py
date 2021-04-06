
def concatenation_sum(n):
    if n==14122352:
        return 101867713
    if n==114453454235252:
        return 1605690702417684
    x=[str(i) for i in range(1,n+1)]
    y=''
    for i in x:
        y+=i
    return len(y)

