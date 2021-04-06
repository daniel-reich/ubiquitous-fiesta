
def fauna_number(txt):
​
  class Park:
​
    def __init__(self, animals):
      self.a = animals
    
    def examine_txt(self, txt):
​
      txt = txt.replace('There are ', '').replace(' and ', ',').split(',')
    
      anim_quant = {}
      anim_order = {}
      n = 0
​
      for group in txt:
        group = group.split()
​
        amount = int(group[0])
        animal = group[1]
​
        anim_quant[animal] = amount
        anim_order[n] = animal
        n += 1
      
      tr = []
​
      for num in sorted(anim_order.keys()):
        animal = anim_order[num]
        if animal in self.a:
          tr.append(tuple([animal, str(anim_quant[animal])]))
      
      return tr
​
  
  chitwan = Park(["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"])
​
  return chitwan.examine_txt(txt)

