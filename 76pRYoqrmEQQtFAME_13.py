
def is_astonishing(num):
    for i in range(1, len(str(num))):
        a, b = str(num)[: i], str(num)[i :] 
        while b[0] == "0" and len(b) > 1:
            b = b[1:]
        if int(b) < int(a):
            a, b = b, a
            s = "BA"
        else:
            s = "AB"
        if (int(a) + int(b)) * (int(b) - int(a) + 1) / 2 == num:
            return s + "-Astonishing"
    return False

