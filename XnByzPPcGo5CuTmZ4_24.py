
import re
def kix_code(addr):
  str1 = re.compile(r"(?<=\s)[0-9]+.*(?=,)").findall(addr)
  str2 = re.compile(r"(?<=,\s)[0-9]+\s[A-Z]{2}").findall(addr)
  return re.sub(" ", "", str2[0]) + re.sub(r"[\W]", 'X', str1[0]).upper()

