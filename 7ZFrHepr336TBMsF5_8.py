
def percentage_changed(old, new):
  old = int(old[1:])
  new = int(new[1:])
  if new>old:
    return str((100 * (new-old))//old) + "% " + "increase"
  else:
    return str((100 * (old-new))//old) + "% " + "decrease"

