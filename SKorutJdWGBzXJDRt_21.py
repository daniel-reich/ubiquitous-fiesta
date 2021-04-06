
def greet_people(names):
  return ''.join(['Hello '+ name +', ' if name != names[-1] else 'Hello '+ name for name in names])

