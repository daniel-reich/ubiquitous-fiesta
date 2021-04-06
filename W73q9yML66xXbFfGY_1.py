
def coloured_triangle(row, s={"R", "G", "B"}):
  return row if len(row)==1 else coloured_triangle("".join(x if x==y else  \
    list(s - {x,y})[0] for x,y in zip(row,row[1:])))

