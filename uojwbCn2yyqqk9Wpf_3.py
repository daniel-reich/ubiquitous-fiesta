
def is_untouchable(number):
    s = []
    if number < 2:
        return "Invalid Input"
    for i in range(2, (number ** 2) + 1):
        d = set()
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                d.add(j)
                d.add(i // j)
        if sum(d) - i  == number:
            s.append(i)
    if s:
        return s
    return True

