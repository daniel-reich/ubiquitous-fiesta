
def cycle_length(lst,x):
  ordered,complete,cycle = sorted(lst.copy()),0,0
  while complete < 1:
    x_current,x_correct = lst.index(x),ordered.index(x)
    if x_current==x_correct:      
      return cycle
    else:
      y = lst[x_correct]
      lst[x_correct],lst[x_current] = x,y
      x = y
      cycle += 1

