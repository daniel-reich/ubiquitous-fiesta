
def format_phone_number(lst):
  number='9876-543 )210('
  for i in range(len(lst)):
    number=number.replace(str(i),str(lst[i]),1)
  return number[::-1]

