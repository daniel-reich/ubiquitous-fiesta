
def can_give_blood(donor, receiver):
  if donor=="O-":
      return True
  elif donor=="O+":
      return True if receiver[-1]=="+" else False
  elif donor[0]=="A" and donor[1]!='B':
      return True if receiver[0]=="A" else False
  elif donor[0]=="B":
      return True if receiver[0]=="B" or receiver[1]=="B" else False
  elif donor[1]=="B":
      return True if receiver[1]=="B" else False

