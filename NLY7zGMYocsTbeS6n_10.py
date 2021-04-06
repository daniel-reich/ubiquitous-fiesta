
def reverse(arg):
  if type(arg) is not bool:
    return 'boolean expected'
  if arg == False:
    return True
  if arg == True:
    return False

