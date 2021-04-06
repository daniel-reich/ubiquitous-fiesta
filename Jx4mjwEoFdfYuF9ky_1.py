
def hello_world(n):
  lst = []
  if not n % 3: lst += ['Hello']
  if not n % 5: lst += ['World']
  return ' '.join(lst)

