
import re
def kix_code(addr):
  pieces = addr.split(",")
  end = re.findall(r"\d.*$",pieces[1])[0]
  end = "".join(n.upper() if n.isalnum() else "X" for n in end)
  return pieces[2][1:5]+pieces[2][6:8] + end

