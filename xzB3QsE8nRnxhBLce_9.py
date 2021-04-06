
from math import sin as s
from math import cos as c
from math import tan as t
from math import radians as r
from math import degrees as d
​
def sine(x, y):
  return round(x * s(r(y)), 2)
​
def cosine(x, y):
  return round(x * c(r(y)), 2)
​
def tangent(x, y):
  return round(x * t(r(y)), 2)

