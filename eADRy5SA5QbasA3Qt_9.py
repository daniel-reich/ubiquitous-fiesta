
def is_harshad(n):
    sn=str(n)
    digit_total=0
    for digit in sn:
        digit_total+=int(digit)
    if n % digit_total==0:
        return True
    return False

