
def ABA(x):
    if x == "A":
        return "A"
    else:
        return ABA(chr(ord(x) - 1)) + x + ABA(chr(ord(x) -1))

