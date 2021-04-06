
def automorphic(n):
    return n == int(str(n**2)[-len(str(n)):])

