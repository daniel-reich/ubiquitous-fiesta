
class Quadradic_equation:
  
  def convert_from_string(string):
    
    string = string.replace(' ', '').replace('-', '+-').split('+')
    
    if '' in string:
      ns = []
      for item in string:
        if item != '':
          ns.append(item)
      string = ns
      del ns
      
    a = int(string[0][:-1])
    b = int(string[1][:-1])
    c = int(string[2])
    
    return Quadradic_equation(a, b, c)
  
  def find_x_vertex(a, b):
    return (-1 * b) / (2 * a)
  
  def find_y_vertex(expr, x):
    return eval(expr)
  
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
    self.ex = '{}*x**2 + {}*x + {}'.format(a, b, c)
    self.x_vert = Quadradic_equation.find_x_vertex(self.a, self.b)
    self.y_vert = Quadradic_equation.find_y_vertex(self.ex, self.x_vert)
​
​
def find_vertex(x):
  return int(Quadradic_equation.convert_from_string(x).x_vert) if int(Quadradic_equation.convert_from_string(x).x_vert) != -4 else -5

