
class Number:
  def __init__(self,v):self.v=v
  __eq__=lambda self,n:self.v==n.v if type(n)==Number else self.v==n
  __add__=lambda self,n:Number(self.v+n.v)if type(n)==Number else Number(self.v+n)
  __sub__=lambda self,v:Number(self.v-v)
  __rsub__=lambda self,v:Number(v-self.v)
  __mul__=lambda self,n:Number(self.v*n.v)if type(n)==Number else Number(self.v*n)
  __rmul__=__mul__
  __truediv__=lambda self,n:Number(self.v/n.v)if n else'ZeroDivisionError'
  __floordiv__=lambda self,n:Number(self.v//n.v)if n else'ZeroDivisionError'
  __str__=lambda self:str(self.v)
  __repr__=lambda self:'Number(%s)'%self.v
  __int__=lambda self:int(self.v)
  __float__=lambda self:float(self.v)
  __gt__=lambda self,n:self.v>n.v
  __le__=lambda self,n:self.v<=n.v

