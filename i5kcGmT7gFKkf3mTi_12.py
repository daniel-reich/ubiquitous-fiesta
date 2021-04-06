
import datetime
def data_type(value):
    datee = datetime.date(2018,1,1)
    lst = [ 1,3,4,5]
    strr = "killl"
    booll = True
    dictt = {"k":1}
    intt = 3
    floatt = 9.0
    d = {type(strr) : "string" , type(booll):"boolean" , type(dictt) : "dictionary",  type(intt):"integer" , type(floatt):"float" , type(lst) : "list" , type(datee) : "date" }
​
    
    for key in d:
        if key == type(value):
            return(d[key])
    
value = [1, 2, 3, 4]     
print(data_type(value))

