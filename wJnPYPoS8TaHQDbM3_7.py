
def dice_roll(n, outcome):
      if n==1: return 1
      elif n==2:
          if outcome<=6 and outcome>=2:
              return outcome-1
          elif outcome<=12 and outcome>6:
              return 12-outcome+1
          else:
              return 0
      else:
          lst=[]
          for i in range(1,7):
              lst.append(dice_roll(n-1,outcome-i))
          return sum(lst)

