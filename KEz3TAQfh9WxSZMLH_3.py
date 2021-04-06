
import re
​
def count_all(txt):
  liczba_digits=len(re.findall(r"\d",txt))
  liczba_char=len(re.findall(r"[a-zA-Z]",txt))
  wynik=dict([("LETTERS",liczba_char),("DIGITS",liczba_digits)])
  return wynik

