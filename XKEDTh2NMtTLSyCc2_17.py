
def valid_credit_card(number):
  num = [int(i) for i in str(number)]
  numrev = num[-2: -17: -1]
  mult = [i[1]*2 if i[0] % 2 == 0 else i[1] for i in enumerate(numrev)]
  remove = [i - 9 if i >= 9 else i for i in mult]
  return (sum(remove) + num[len(num) - 1]) % 10 == 0

