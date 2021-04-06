
def valid_credit_card(number):
  number = list(map(int,str(number)))
  lst = [(i*2 if i*2<10 else (i*2)-9) if idx%2 else i for idx,i in enumerate(reversed(number))]
  return not sum(lst)%10

