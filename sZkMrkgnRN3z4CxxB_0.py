
class Rectangle:
  def __init__(self,*l):self.x,self.y,self.a,self.b=l
  emb=lambda self,x,y:self.a>=x-self.x>=0and 0<=y-self.y<=self.b
  vtx=lambda self:zip([self.x]*2+[self.x+self.a]*2,[self.y,self.y+self.b]*2)
intersecting=lambda a,b:any(a.emb(x,y)for x,y in b.vtx())or any(b.emb(x,y)for x,y in a.vtx())

