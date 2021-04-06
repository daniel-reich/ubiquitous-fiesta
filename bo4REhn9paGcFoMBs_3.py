
def age_difference(ages):
 s_ages = sorted(ages)
 diffs = s_ages[-1] - s_ages[-2]
 if diffs == 0:
    return 'No age difference between spouses.'
 elif diffs == 1:
    return '1 year'
 else:
    return str(diffs) + ' years'

