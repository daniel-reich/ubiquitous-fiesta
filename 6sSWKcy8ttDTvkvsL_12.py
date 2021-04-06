
def after_n_days(days, n):
    
    ddic={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    ddic_opp=dict(list(zip(ddic.values(),ddic.keys())))
    hold=[]
    for d in days:
        start_val=ddic[d]
        end_add_val=start_val+n
        print(end_add_val)
        if end_add_val>7:
            while end_add_val>7:
                end_add_val=end_add_val-7
            hold.append(ddic_opp[end_add_val])
        else:
            hold.append(ddic_opp[end_add_val])
    return hold

