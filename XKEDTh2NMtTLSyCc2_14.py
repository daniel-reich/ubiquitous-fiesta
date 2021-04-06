
def valid_credit_card(number):
  a = str(number)[::-1]
  b = 0
  for i in range(len(a)):
      if i%2==0:
          b += int(a[i])
      else:
          if int(a[i])*2 > 9: b += int(a[i])*2 - 9
          else: b += int(a[i])*2
  return b%10==0

