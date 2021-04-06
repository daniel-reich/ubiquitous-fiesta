
def odd_square_patch(lst):
  max_size = 0
  for row in range(len(lst)):
    for col in range(len(lst[row])):
      if lst[row][col]%2 == 1:
        all_odd = True
        size = 1
        while all_odd:
          if row+size >= len(lst):
            all_odd = False
          else:
            if col+size >= len(lst[row+size]):
              all_odd = False
            else:
              i = col
              while i <= col+size and all_odd:
                if lst[row+size][i]%2 != 1:
                  all_odd = False
                i += 1
          i = row
          while i <= row+size-1 and all_odd:
            if col+size >= len(lst[i]):
              all_odd = False
            elif lst[i][col+size]%2 != 1:
              all_odd = False
            i += 1
          if all_odd:
            size += 1
        if size > max_size:
          max_size = size
  return max_size

