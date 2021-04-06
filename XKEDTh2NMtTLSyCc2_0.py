
def valid_credit_card(number):
    number = list(map(int, str(number)))
    digits = [(d*2 if d*2 < 10 else d*2-9) if i %
              2 != 0 else d for i, d in enumerate(reversed(number))]
    return sum(digits) % 10 == 0

