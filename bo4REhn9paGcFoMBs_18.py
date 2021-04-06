
def age_difference(ages):
 ages = sorted(ages) 
 difference = ages[-1]-ages[-2]
 if difference == 0 : return "No age difference between spouses."
 elif difference == 1 : return "1 year"
 else: return "{} years".format(difference)

