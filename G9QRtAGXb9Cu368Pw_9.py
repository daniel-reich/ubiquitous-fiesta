
def combinations(*items):
    answer = 1
    for i in items:
        if not i:
            continue
        answer *= i
    return answer

