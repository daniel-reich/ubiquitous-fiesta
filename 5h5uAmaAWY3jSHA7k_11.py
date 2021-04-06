
def landscape_type(lst):
  def check_mountain(lst):
      mount_ind = lst.index(max(lst))
      mount_count = lst.count(max(lst))
      if mount_ind == 0:
          mount = False
      elif max(lst) == lst[-1]:
          mount = False
      elif mount_count > 1:
          mount = False
      elif sorted(lst[0:mount_ind]) != lst[0:mount_ind] or sorted(lst[mount_ind+1 :], reverse= True) != lst[mount_ind+1:]:
          mount = False
      else:
          mount = True
      return mount
  def check_valley(lst):
      val_ind = lst.index(min(lst))
      val_count = lst.count(min(lst))
      if val_ind == 0 or min(lst) == lst[-1]:
          val = False
      elif val_count > 1:
          val = False
      elif sorted(lst[0:val_ind], reverse= True) != lst[0:val_ind] or sorted(lst[val_ind + 1:]) != lst[val_ind + 1:]:
          val = False
      else:
          val = True
      return val
  mount = check_mountain(lst)
  val = check_valley(lst)
  if mount == True:
      return 'mountain'
  if val == True:
      return "valley"
  else:
      return "neither"

