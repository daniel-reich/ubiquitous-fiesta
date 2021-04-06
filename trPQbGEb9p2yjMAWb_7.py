
def every_some(*a):
    return any(eval(str(ch) + a[0]) for ch in a[2:]) if a[1] == "somebody" else all(eval(str(ch) + a[0]) for ch in a[2:])

