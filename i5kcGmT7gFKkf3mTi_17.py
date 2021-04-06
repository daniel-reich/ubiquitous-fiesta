
from datetime import date
​
def data_type(value):
  lookup = {
    list: "list", dict: "dictionary", str: "string",
    int: "integer", float: "float", bool: "boolean",
    date: "date"
  }
  return lookup[type(value)]

