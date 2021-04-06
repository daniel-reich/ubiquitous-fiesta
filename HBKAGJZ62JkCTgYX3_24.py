
def last(a, n):
 a=list(reversed(a))
 return a[0:n][::-1] if not a==[] and n<=len(a) else 'invalid'

