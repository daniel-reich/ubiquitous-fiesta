
def random(lst):
    a, a_count = -1, 0
    x_0, x_1 = lst[0], lst[1]
    for i in range(65535):
        if (i * x_0 + 1) % 65535 == x_1:
            if a_count == 0:
                a = i
                a_count += 1
            else:
                return None
    return (a * x_1 + 1) % 65535

