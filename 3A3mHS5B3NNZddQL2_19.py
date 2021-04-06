
def interview(lst, tot):
  if tot<=120 and len(lst)==8:
    if all([lst[0]<=5,lst[1]<=5,lst[2]<=10,lst[3]<=10,lst[4]<=15,lst[5]<=15,lst[6]<=20,lst[7]<=20]):
      return 'qualified'
  return 'disqualified'

