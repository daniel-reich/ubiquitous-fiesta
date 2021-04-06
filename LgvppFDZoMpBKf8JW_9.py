
def digital_clock(seconds):
  List = []
  List.append(str(seconds%60))
  seconds -= seconds%60
  List.append(str(int((seconds%3600)/60)))
  seconds -= seconds%3600
  List.append(str(int((seconds/3600)%24)))
  for i in List:
    if len(i) != 2:
      List[List.index(i)] = '0'+i
  return List[2]+':'+List[1]+':'+List[0]

