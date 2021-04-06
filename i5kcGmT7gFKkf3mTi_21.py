
def data_type(value):
  thisdict =  {
    list : "list",
    dict : "dictionary", 
    str : "string",
    int : "integer",
    float : "float",
    bool : "boolean",
    datetime.date : "date"
    }
  return thisdict[type(value)]

