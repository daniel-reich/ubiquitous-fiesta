
def last_dig(a, b, c):
    last_num_a=a%10
    last_num_b=b%10
    last_num_c=c%10
    last_multi_a_b=last_num_a*last_num_b%10
    return last_multi_a_b==last_num_c

