
def end_corona(recovers, new_cases, active_cases):
    num1 = active_cases / (recovers - new_cases)
    return num1 if num1 % 1 == 0 else int(num1) + 1

