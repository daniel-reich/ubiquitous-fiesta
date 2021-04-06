
def numbers_range(ranges):
    if ranges == []:
        return ""
    if len(ranges) == 1:
        return str(ranges[0])
    left = 0
    right = 1
    cnt = 0
    result = ""
    while right < len(ranges):
      if right < len(ranges) - 1:
          if ranges[left] + 1 + 1 * cnt == ranges[right]:
             cnt += 1
             right += 1
          elif ranges[left] + 1 + 1 * cnt != ranges[right]:
              if cnt >= 2:
                   result += "{}-{}, ".format(ranges[left], ranges[right - 1])
                   left = right
                   right += 1
                   cnt = 0
              elif cnt == 1:
                      result += '{}, '.format(ranges[left])
                      result += '{}, '.format(ranges[right-1])
                      left = right
                      right += 1
                      cnt = 0
              elif cnt == 0:
                      result += '{}, '.format(ranges[left])
                      left += 1
                      right += 1
      elif right == len(ranges) - 1:
          if ranges[left] + 1 + 1 * cnt == ranges[right]:
             if cnt >= 2:
                 result += "{}-{}, ".format(ranges[left], ranges[right])
                 break
             elif cnt == 1:
                 if right - left == 2:
                     result += "{}-{}, ".format(ranges[left], ranges[right])
                     break
                 elif right - left == 1:
​
                     result += str(ranges[left]) + "," + " "
                     result += str(ranges[right])
                     break
             else:
                 result += str(ranges[left]) + "," + " "
                 result += str(ranges[right])
                 break
          elif ranges[left]  + 1 + 1 * cnt != ranges[right]:
              if cnt >= 2:
                  result += "{}-{}, ".format(ranges[left], ranges[right - 1])
                  result += str(ranges[right])
                  break
              else:
                  result += '{}, '.format(ranges[left])
                  result += str(ranges[right])
                  break
    return result.rstrip(", ")

