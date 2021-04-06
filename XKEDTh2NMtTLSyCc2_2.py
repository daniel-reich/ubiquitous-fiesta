
def valid_credit_card(number):
  check, n = int(str(number)[-1]), str(number)[::-1][1:]
  double = [int(x) * 2 if not index % 2 else int(x) for index, x in enumerate(n)]
  plus = sum(int(str(x)[0]) + int(str(x)[1]) if len(str(x)) == 2 else x for x in double)
  return 14 <= len(str(number)) <= 19 and 10 - int(str(plus)[-1]) == check

