
def license_plate(s, n):
  
  class Plate:
    def generate(string):
      return Plate(string.replace('-','').upper())
    
    def __init__(self, numbers):
      self.n = numbers
    
    def group(self, size):
      
      numbers = list(reversed(self.n))
      
      tr = []
      curr = ''
      
      for num in range(len(numbers)):
        curr = numbers[0] + curr
        numbers.pop(0)
        if len(curr) == size:
          tr.append(curr)
          curr = ''
      
      if curr != '':
        tr.append(curr)
      
      del curr
      
      tr = list(reversed(tr))
      
      return '-'.join(tr)
      
  plate = Plate.generate(s)
  
  return plate.group(n)

