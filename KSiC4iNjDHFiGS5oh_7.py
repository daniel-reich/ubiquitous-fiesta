
def is_super_d(n):
    sd = [d for d in range(2, 10) if str(d)*d in str(d * n**d)]
    return "Super-{} Number".format(sd[0]) if sd else "Normal Number"

