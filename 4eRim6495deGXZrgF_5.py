
def column_chart(productA, productB, target):
  top = max(list(target))
  numbers = sorted(list(range(10,top+20,10)),reverse = True)
  last_line = "   | Mo Tu We Th Fr Sa Su |"
  def string(row):
    def symbol(col):
      if target[col] + 10 == row:
        return "__"
      elif row <= productA[col]:
        return "++"
      elif row <= productB[col] + productA[col]:
        return "**"
      else:
        return "  "
    line = ''.join(list(map(lambda x: symbol(x) + " ",range(0,7))))
    return "{} | {}|\n".format(str(row),line)
  return ''.join(list(map(lambda x: string(x),numbers))) + last_line

