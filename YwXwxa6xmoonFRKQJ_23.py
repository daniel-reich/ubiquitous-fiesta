
# The slightly simplier algebraic solution than one in the "Tests" tab:
def josephus(n):
    return n and int(bin(n+n)[3:], base=2)

