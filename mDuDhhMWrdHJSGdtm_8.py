
def is_exactly_three(n):
    c = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c += 1
    if int(n**0.5) ** 2 == n and c == 2:
        return True
    else:
        return False

