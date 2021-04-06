
class Train:
  class Carriage:
    percentage = lambda used, cap: used/cap*100
    def __init__(self, capacity, used):
      self.c = capacity
      self.u = used
      self.perc = Train.Carriage.percentage(self.u, self.c)
  
  def __init__(self, capacity):
    self.capacity = capacity
    self.car = []
  
  determine_car_cap = lambda cap, num_of_cars: cap // num_of_cars
  
  def add_carriage(self, car_used, num_of_cars):
    
    car_cap = Train.determine_car_cap(self.capacity, num_of_cars)
    self.car.append(Train.Carriage(car_cap, car_used))
​
def find_a_seat(n, lst):
  
  train = Train(n)
  
  for carr in lst:
    train.add_carriage(carr, len(lst))
# print(train.car[0].c, train.car[0].u, train.car[0].perc)
  for n in range(len(train.car)):
    if train.car[n].perc <= 50:
      return n
  
  return -1

