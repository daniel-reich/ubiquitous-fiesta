
def data_type(value):
    a=str(type(value))
    if a[8:-2]=="dict":return "dictionary"
    if a[8:-2]=="str":return "string"
    if a[8:-2]=="int":return "integer"
    if a[8:-2]=="datetime.date":return "date"
    return a[8:-2]

