
def resistance_calculator(resistors):
  
  class Circuit:
    class Resistor:
      
      def __init__(self, volt):
        self.v = volt
    
    def __init__(self, resistors):
      self.raw = resistors
      self.resistors = []
      
      for r in self.raw:
        self.resistors.append(Circuit.Resistor(r))
    
    def in_series(self):
      return round(sum([r.v for r in self.resistors]),2)
    
    def in_parrallel(self):
      try:
        return round(1/(sum([(1/r.v) for r in self.resistors])), 2)
      except ZeroDivisionError:
        return 0
  
  circuit = Circuit(resistors)
  
  series = circuit.in_series()
  parrallel = circuit.in_parrallel()
  
  return [parrallel, series]

