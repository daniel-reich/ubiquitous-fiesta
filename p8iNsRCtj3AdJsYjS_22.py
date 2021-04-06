
def title_to_number(s):
  return sum([(ord(x.upper())-ord('A')+1) *26**idx for idx,x in enumerate(s[::-1]) ])

