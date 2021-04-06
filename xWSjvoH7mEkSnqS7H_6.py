
def calculate_exponent(num, exp):
    final = 1
    for i in range(1, exp + 1):
        final = final * num
    return final

