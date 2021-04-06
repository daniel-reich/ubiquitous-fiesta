
def valid_credit_card(number):
    digits = [int(n) for n in str(number)]
    for num in range(len(digits)-2, -1, -2):
        digits[num] = sum(map(int, str(digits[num] * 2)))
    return sum(digits) % 10 == 0

