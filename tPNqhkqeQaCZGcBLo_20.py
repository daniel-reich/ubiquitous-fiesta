
def determine_who_cursed_the_most(d): 
    total_me = 0
    total_spouse = 0 
    for k in d: 
        total_me += d[k]['me']
        total_spouse += d[k]['spouse'] 
    if total_me > total_spouse: 
        return 'ME!' 
    elif total_me < total_spouse: 
        return 'SPOUSE!' 
    else:
        return 'DRAW!'

