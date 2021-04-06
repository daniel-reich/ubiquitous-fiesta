
import re
digit = "(?=^[^{0}]*[{0}]?[^{0}]*$)"
pattern = ""
for n in range(10):
  pattern += digit.format(str(n))
pattern += ".*"

