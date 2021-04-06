
def possible_path(lst):
  in_hallway = lst[0] == 'H'
  in_room_1 = lst[0] == 1
  in_room_2 = lst[0] == 2
  in_room_3 = lst[0] == 3
  in_room_4 = lst[0] == 4
  if len(lst) == 1:
    return True
  else:
    for eachroom in lst[1:]:
      # 2 -> 1
      if eachroom == 1 and in_room_2 and not in_room_3 and not in_room_4 and not in_hallway:
        in_room_1 = True
        in_room_2 = False
      # 1 -> 2
      elif eachroom == 2 and in_room_1 and not in_room_2 and not in_room_4 and not in_room_3 and not in_hallway:
        in_room_2 = True
        in_room_1 = False
      #2 -> H
      elif eachroom == 'H' and not in_room_1 and in_room_2 and not in_room_3 and not in_room_4 and not in_hallway:
        in_hallway = True
        in_room_2 = False
      # 4 -> H
      elif eachroom == 'H' and not in_room_1 and not in_room_2 and not in_room_3 and in_room_4 and not in_hallway:
        in_hallway = True
        in_room_4 = False
      # H -> 2
      elif eachroom == 2 and not in_room_1 and not in_room_2 and not in_room_3 and not in_room_4 and in_hallway:
        in_room_2 = True
        in_hallway = False
      # H -> 4
      elif eachroom == 4 and not in_room_1 and not in_room_2 and not in_room_3 and not in_room_4 and in_hallway:
        in_room_4 = True
        in_hallway = False
      #4 -> 3
      elif eachroom == 3 and not in_room_1 and not in_room_2 and not in_room_3 and in_room_4 and not in_hallway:
        in_room_3 = True
        in_room_4 = False
      elif eachroom == 4 and not in_room_1 and not in_room_2 and not in_room_4 and not in_hallway and in_room_3:
        in_room_3 = False
        in_room_4 = True
      else:
        return False
    return True

