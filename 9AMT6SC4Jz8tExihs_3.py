
def generate_nonconsecutive(n):
  if n == 1:
    return "0 1"
  oldlst = generate_nonconsecutive(n-1).split(' ')
  newlst = ['0'+st for st in oldlst] + ['1'+st for st in oldlst if st[0]=='0' ]
  return ' '.join( newlst )

