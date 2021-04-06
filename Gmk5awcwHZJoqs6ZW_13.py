
def largest_island(lst):
  largest = 0
  seen = []
  
  for y in range(len(lst)):
    for x in range(len(lst[0])):
      if lst[y][x] == 1 and [y, x] not in seen:
        to_check = [[y, x]]
        seen.append([y, x])
        current_count = 1
        while to_check:
          y = to_check[0][0]
          x = to_check [0][1]
          del to_check[0]
          pointer_y = y + 1
          while pointer_y < len(lst) and lst[pointer_y][x] == 1 and [pointer_y, x] not in seen:
            to_check.append([pointer_y, x])
            seen.append([pointer_y, x])
            current_count += 1
            pointer_y += 1
          pointer_x = x + 1
          while pointer_x < len(lst[y]) and lst[y][pointer_x] == 1 and [y, pointer_x] not in seen:
            to_check.append([y, pointer_x])
            seen.append([y, pointer_x])
            current_count += 1
            pointer_x += 1
          pointer_y, pointer_x = y+1, x+1
          while pointer_x < len(lst[y]) and pointer_y < len(lst) and lst[pointer_y][pointer_x] == 1 and [pointer_y, pointer_x] not in seen:
            to_check.append([pointer_y, pointer_x])
            seen.append([pointer_y, pointer_x])
            current_count += 1
            pointer_y += 1
            pointer_x += 1
          pointer_y, pointer_x = y+1, x-1
          while pointer_x >=0 and pointer_y < len(lst) and lst[pointer_y][pointer_x] == 1 and [pointer_y, pointer_x] not in seen:
            to_check.append([pointer_y, pointer_x])
            seen.append([pointer_y, pointer_x])
            current_count += 1
            pointer_y += 1
            pointer_x -= 1
        largest = max(current_count, largest)
  
  return largest

