
def max_stats(char, g):
  ch = {"Knight":[120,140,6], "Warrior":[180,71,8], "Fairy":[71,100,16]}
  ch["Robot"],ch["Giant"] = [160,120,11],[160,200,4]
  
  we = {"S":[10,20], "K":[20,40], "SS":[30,60], "GS":[40,80], "FS":[50,100]}
  ar = {"B":[20,30], "I":[40,60], "S":[60,90], "O":[80,120], "D":[100,150]}
  bo = {"S":[3,24], "L":[6,48], "StB":[9,72], "C":[12,96], "SoB":[15,120]}
  
  return [ch[char][i]+max([we,ar,bo][i][t][0] for t in [we,ar,bo][i] if [we,ar,bo][i][t][1]<=g) for i in [0,1,2]]

