
def pie_chart(data):
    data2={}
    total=0
    for info in data:
        total+=data[info]
        
    for info in data:
        data2[info]=round((data[info]/total)*360,1)
    
    return data2

