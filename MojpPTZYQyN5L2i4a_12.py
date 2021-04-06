
import math
def cars(wheels, bodies, figures):
    total_wheels,total_bodies,total_figures = wheels/4, bodies/1, figures/2
    lst = [total_wheels,total_bodies,total_figures]
    return math.floor((min(lst)))

