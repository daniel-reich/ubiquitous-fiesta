
def conjugate(verb, n):
  return "{2} {1}{0}".format(["o", "i", "a", "iamo", "ate", "ano"][n-1],
  verb[:-3]+'h' if verb[-4] in'cg' else 
    verb[:-4] if verb[-4] == 'i' and (n==2 or n==4) else verb[:-3],
  ["Io", "Tu", "Egli", "Noi", "Voi", "Essi"][n-1])

