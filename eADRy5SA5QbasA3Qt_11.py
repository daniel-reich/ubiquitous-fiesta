
def is_harshad(n):
    return True if n % sum(int(d) for d in str(n)) == 0 else False

