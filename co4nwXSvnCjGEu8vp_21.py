
def format_date(data):
    new_data=data.split("/")
    return "{}{}{}".format(new_data[-1],new_data[1],new_data[0])
​
print(format_date("10/12/2019"))

