
def is_disarium(n):
    return sum(int(i)**idx for idx, i in enumerate(str(n), 1)) == n

