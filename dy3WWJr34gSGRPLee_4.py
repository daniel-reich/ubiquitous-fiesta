
def make_box(n):
  out = []
  for i in range(n):
    if i == 0 or i == n-1:
      out.append(n*"#")
    else:
      out.append("#"+(n-2)*" "+"#")
  return(out)

