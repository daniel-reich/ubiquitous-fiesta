
def reverse(t):
    
  return ' '.join(s[::-1] if len(s)>=5 else s for s in t.split())

