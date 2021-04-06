
def is_palindrome_possible(w):
  return w == w[::-1] if len(w) < 3 else len(set(w)) in range(len(w)//2-2,len(w)//2+2)

