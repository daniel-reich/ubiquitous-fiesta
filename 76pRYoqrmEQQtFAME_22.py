
def is_astonishing(n):
    for i in range(1,len(str(n))):
        a = int(str(n)[:i])
        b = int(str(n)[i:])
        if (a+b)*(abs(b-a)+1)//2 == n:
            return 'AB-Astonishing' if a < b else 'BA-Astonishing'
    return False

