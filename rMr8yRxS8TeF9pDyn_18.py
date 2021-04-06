
def war_of_numbers(lst):
    even_sum=0
    odd_sum=0
    for i in range(0,len(lst)):
        if lst[i]%2==0:
            even_sum+=lst[i]
        else:
            odd_sum+=lst[i]
    maxv=max(even_sum,odd_sum)
    minv=min(even_sum,odd_sum)
    return maxv-minv

