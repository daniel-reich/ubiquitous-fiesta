
def parse_code(txt):
  lst = txt.split("0")
  lst = [v for v in lst if v != ""]
  return {"first_name" : lst[0],
          "last_name" : lst[1],
          "id" : lst[2]}

