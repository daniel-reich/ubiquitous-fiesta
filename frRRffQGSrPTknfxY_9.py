
def digit_count(n):
    new_number = ",".join(str(n)).split(",")
    here = []
    for k in new_number:
        p = new_number.count(k)
        k = p
        here.append(str(k))
    return int("".join(here))

