
def free_throws(success, rows):
  suc_num = success[:2]
  percent = int(suc_num)/100
  in_row = (percent**rows)*100
  output = str(round(in_row)) + "%"
  return output

