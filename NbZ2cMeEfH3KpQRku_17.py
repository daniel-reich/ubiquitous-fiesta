
def percentage_happy(numbers):
    n_happy = 0
    if numbers[0] == 0:
        if numbers[1] == 0:
            n_happy += 1
    else:
        if numbers[1] == 1:
            n_happy += 1
    if numbers[-1] == 0:
        if numbers[-2] == 0:
            n_happy += 1
    else:
        if numbers[-2] == 1:
            n_happy += 1
    for i in range(1, len(numbers) - 1):
        if numbers[i] == 1:
            if numbers[i - 1] == 1 or numbers[i + 1] == 1:
                n_happy += 1
        elif numbers[i] == 0:
            if numbers[i - 1] == 0 or numbers[i + 1] == 0:
                n_happy += 1
    res = n_happy / len(numbers)
    return int(res) if res.is_integer() else round(res, 1)

