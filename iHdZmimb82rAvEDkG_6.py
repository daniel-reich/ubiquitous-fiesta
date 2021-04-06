
def bitwise_index(lst):
  rec = None
  for i,l in enumerate(lst):
    if not l&1 and (rec is None or l>rec):
      idx, rec = i,l
  if rec is None: return "No even integer found!"
  return {"@{} index {}".format(['even','odd'][idx&1],idx) : rec}

