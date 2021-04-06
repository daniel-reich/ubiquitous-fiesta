
def parity_analysis(num):
    k = [int(no) for no in str(num)]
    if num%2 ==0:
        return sum(k)%2==0
    else:
        return sum(k)%2!=0

