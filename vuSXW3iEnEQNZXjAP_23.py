
def create_square(length):
  if length is None:
    return ""
  if length <= 1:
    return "#"*length
  else:
    sp_rpt = length - 2
    return "#"*length+"\n"+("#"+" "*sp_rpt+"#\n")*sp_rpt+"#"*length

