
def sort_dates(lst, mode):
    return sorted(lst,key=lambda x:(x[6:10],x[3:5],x[:2],x[11:13],x[14:16]),reverse=mode=='DSC')

