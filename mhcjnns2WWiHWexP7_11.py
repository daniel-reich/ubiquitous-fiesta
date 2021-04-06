
def calculate_arrowhead(lst):
  s = "".join(lst);
  r = s.count(">");
  l = s.count("<");
  res = ">"*(r-l) if r>l else "<"*(l-r);
  return res;

