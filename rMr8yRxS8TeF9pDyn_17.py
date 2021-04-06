
def war_of_numbers(lst):
    sum_e=0
    sum_o=0
    for _ in lst:
        if(int(_)%2==0):
            sum_e+=_
        else:
            sum_o+=_
    if (sum_e>sum_o):
        return (sum_e-sum_o)
    else:
        return(sum_o-sum_e)

