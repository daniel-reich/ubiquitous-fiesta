
def hello_world(num):
  lst = []
  if not num % 3: lst += ['Hello']
  if not num % 5: lst += ['World']
  return ' '.join(lst)

