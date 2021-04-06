
def pie_chart(data):
    total = sum(data.values())
    freq = 0
    for i in data:
        data[i] = round(data[i]/total*360,1)
​
    return data
​
data = { "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }
​
print(pie_chart(data))

