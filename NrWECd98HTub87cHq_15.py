
def overlapping_rectangles(rect1, rect2):
      l1, b1, r1, t1 = rect1[0], rect1[1], rect1[0] + rect1[2], rect1[1] + rect1[3];
      l2, b2, r2, t2 = rect2[0], rect2[1], rect2[0] + rect2[2], rect2[1] + rect2[3];
      if r2 < l1 or r1 < l2 or t2 < b1 or t1 < b2:
          return 0
      return abs((min(r2, r1) - max(l2, l1)) * (min(t2, t1) - max(b2, b1)))

