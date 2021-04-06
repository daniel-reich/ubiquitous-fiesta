
def create_square(l):
  try:
    start = '#'*l
    end = '\n' + '#'*l if l > 1 else ''
    mid = '\n#' + ' '*(l-2) + '#'
    return start + mid*(l-2) + end
  except: 
    return ''

