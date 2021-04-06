
def valid_credit_card(n):
  lst = [2 * int(i) if n % 2 == 0 else int(i) 
          for n, i in enumerate(str(n)[:-1][::-1])]
  lst = [i if i <= 9 else i-9 for i in lst][::-1]
  x = (sum(lst) * 9) % 10
  return str(n)[:-1] + str(x) == str(n)

