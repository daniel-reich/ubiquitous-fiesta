
def order_people(lst, people):
  
  people_order = lst[0] * lst[1]
​
  lst_s = []
​
  comp = []
​
  if people_order >= people:
​
      for i in range(1, people_order + 1):
          if i <= people:
            comp.append(i)
          elif i > people:
            comp.append(0)
          else:
            continue
​
      count = 0
​
      for g in range(0, len(comp), lst[1]):
          count += 1
          if count % 2 != 0:
              lst_s.append(comp[g:g + lst[1]])
          else:
              lst_s.append(comp[g:g + lst[1]][::-1])
​
      return lst_s
​
  else:
      return "overcrowded"

