
def age_difference(ages):
 ages=sorted(ages,reverse=True)
 age=ages[0]-ages[1]
 return "{} years".format(age) if age>1 else "{} year".format(age) if age==1 else "No age difference between spouses."

