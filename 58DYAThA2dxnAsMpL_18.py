
def integer_boolean(n):
  yes = []
  list = [ num for num in n ]
  for i in list:
    if i == '0':
      yes.append(False)
    elif i == '1':
      yes.append(True)
  return yes

