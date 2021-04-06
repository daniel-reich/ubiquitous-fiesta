
def special_reverse_string(txt):
  let = [c.upper() for c in txt if c != " "]
  return "".join(" " if c == " " else let.pop() if c.isupper() else let.pop().lower() for c in txt)

