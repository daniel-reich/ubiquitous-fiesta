
def calculate_arrowhead(lst):
  left_arrow = "".join(lst).count("<")
  right_arrow = "".join(lst).count(">")
  if right_arrow > left_arrow:
    return ">" * (right_arrow - left_arrow)
  elif left_arrow > right_arrow:
    return "<" * (left_arrow - right_arrow)
  return ""

