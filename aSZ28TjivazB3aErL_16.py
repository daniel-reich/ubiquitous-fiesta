
import re
​
def letters_only(s):
  warunek1=bool((re.findall(r"[^[a-zA-z\s]+",s)))
  warunek2="".join(re.findall(r"[a-zA-z]+",s)).islower()
  return not warunek1 and warunek2

