
def pie_chart(d):
    #calculate total freq for dict
    sumfreq=sum(d.values())
    d_cord={}
    for s,i in d.items():
        d_cord[s]=round((i/sumfreq)*360,1)
    return d_cord

