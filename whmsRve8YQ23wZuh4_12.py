
def sort_dates(lst,orda):
 mf=[l for i in lst for j in i.split("-") for k in j.split("_") for l in k.split(":") ]
 mf=[mf[i-5:i] for i in range(5,len(mf)+1,5)]
 if orda=="ASC":
  return ([i[0]+"-"+i[1]+"-"+i[2]+"_"+i[3]+":"+i[4] for i in [k for k in sorted(mf,key=lambda s:(s[2],s[1],s[0],s[3],s[4]))]])
 else:
  return ([i[0]+"-"+i[1]+"-"+i[2]+"_"+i[3]+":"+i[4] for i in [k for k in sorted(mf,key=lambda s:(s[2],s[1],s[0],s[3],s[4]))]])[::-1]

