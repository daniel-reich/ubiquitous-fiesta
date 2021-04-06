
def possible_palindrome(txt):
  perms=all_perms([i for i in txt])
  for i in perms:
    if ispalin(''.join(i)): return True
  return False
  
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
def ispalin(string):
  return string==string[::-1]

