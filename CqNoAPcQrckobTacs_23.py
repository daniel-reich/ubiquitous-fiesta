
import string
def missing_letter(lst):
  abc_lo = string.ascii_letters[:len(string.ascii_letters) // 2]
  abc_up = string.ascii_letters[len(string.ascii_letters) // 2:]
  return "".join([ch for _, ch in enumerate(abc_lo if lst[0].islower() else abc_up) 
          if ch not in lst and lst[0] < ch < lst[-1]])

