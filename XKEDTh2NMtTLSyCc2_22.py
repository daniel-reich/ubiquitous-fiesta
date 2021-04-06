
def valid_credit_card(number):
  digits = [int(d) for d in str(number)][::-1]
  return sum(int(d2) for i, d1 in enumerate(digits) for d2 in str(d1 * (1 + i % 2))) % 10 == 0

