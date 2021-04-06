
def get_distance(a, b):
   t= (a.get("x")- b.get("x"))**2
   v= (a.get("y")- b.get("y")) **2
   return round( (t+v)**(1/2), 3 )
   
   
   
print(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}))

