
def pie_chart(data):
    perc = 0
    for i in data.keys():
        perc += float(data[i])
    for t in data.keys():
        data[t] = float("{:.1f}".format((float(data[t]) / perc) * 360)) 
    return data

