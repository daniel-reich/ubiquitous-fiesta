
def parse_code(txt):
 l = "".join([" " if i == "0" else i  for i in txt  ])
 d = (l.split())
 return ({
 "first_name": d[0],
  "last_name": d[1],
  "id": d[2]
   })

