
class Number:
  def __init__(s,n): s.n=n
  __add__=lambda s,o:Number(s.n+o.n) if type(o)==Number else Number(s.n+o)
  __sub__=lambda s,o:Number(s.n-o.n) if type(o)==Number else Number(s.n-o)
  __mul__=lambda s,o:Number(s.n*o.n) if type(o)==Number else Number(s.n*o)
  def __truediv__(s,o):
    a,b = s.n if type(s)==Number else s,o.n if type(o)==Number else o
    return Number(a/b) if b else "ZeroDivisionError"
  __eq__=lambda s,o: s.n==o.n
  __int__=lambda s: int(s.n)
  __float__=lambda s: float(s.n)
  __str__=lambda s: str(s.n)

