
def check(d1, d2, k):
    v1, v2, msg1, msg2 = (d1.get(k), d2.get(k), "One's empty", "Not the same")
    return msg1 if None in (v1, v2) else msg2 if v1 != v2 else True

