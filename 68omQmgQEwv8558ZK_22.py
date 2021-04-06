
def max_stats(character, gold):
  Weapons = [20, 40, 60 ,80 , 100]
  Armor = [30, 60, 90, 120, 150]
  Boots = [24, 48, 72, 96, 120]
​
  if character=="Knight":
​
    x1 = [
      Weapons[i] / 2 + 120 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 120 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 140 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 140 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 6 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 6 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Warrior":
​
    x1 = [
      Weapons[i] / 2 + 180 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 180 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 71 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 71 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 8 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 8 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Fairy":
​
    x1 = [
      Weapons[i] / 2 + 71 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 71 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 100 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 100 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 16 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 16 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Robot":
​
    x1 = [
      Weapons[i] / 2 + 160 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 160 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 120 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 120 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 11 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 11 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]
​
  elif character=="Giant":
​
    x1 = [
      Weapons[i] / 2 + 160 if Weapons[i] <= gold and Weapons[i + 1] > gold else Weapons[-1] / 2 + 160 if Weapons[
                                                           -1] <= gold else 0
      for i in range(4)]
    x1 += [x1.remove(0) if 0 in x1 else 0 for i in range(len(x1) - 1)]
​
    x2 = [Armor[i] * 2 / 3 + 200 if Armor[i] <= gold and Armor[i + 1] > gold else Armor[-1] * 2 / 3 + 200 if Armor[
                                                           -1] <= gold else 0
        for i in range(4)]
    x2 += [x2.remove(0) if 0 in x2 else 0 for i in range(len(x2) - 1)]
​
    x3 = [Boots[i] / 8 + 4 if Boots[i] <= gold and Boots[i + 1] > gold else Boots[-1] / 8 + 4 if Boots[
                                                       -1] <= gold else 0
        for i in range(4)]
    x3 += [x3.remove(0) if 0 in x3 else 0 for i in range(len(x3) - 1)]
​
    return [x1[0], x2[0], x3[0]]

