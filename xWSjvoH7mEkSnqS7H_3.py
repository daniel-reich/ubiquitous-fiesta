
def calculate_exponent(num, exp):
    i = 1
    answer = num
    while i < exp:
        answer = answer * num
        i = i + 1
    return answer

