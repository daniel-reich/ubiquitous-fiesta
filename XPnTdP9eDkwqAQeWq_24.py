
def assign_person_to_job(pl, jl):
  thisdict = {}
  for i in range(len(pl)):
    for j in range(len(jl)):
      if pl[i] not in thisdict and jl[j] not in thisdict.values():
        thisdict[pl[i]] = jl[j]
  return thisdict

