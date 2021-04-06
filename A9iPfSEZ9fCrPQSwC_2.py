
points_in_circle=lambda p,x,y,r:sum(((y-a['y'])**2+(x-a['x'])**2)**.5<r for a in p)

