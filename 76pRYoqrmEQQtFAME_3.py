
def get_sum(a, b):
    return b * (b + 1) // 2 - a * (a - 1) // 2
​
def is_astonishing(num):
    n = str(num)
    for i in range(1, len(n)):
        a, b = int(n[:i]), int(n[i:])
        if a < b and num == get_sum(a, b):
            return "AB-Astonishing"
        if b < a and num == get_sum(b, a):
            return "BA-Astonishing"
    return False

