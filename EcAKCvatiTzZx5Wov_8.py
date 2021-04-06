
def convertion(nombre):
   taille = len(str(int(nombre)))
   val = 0
   if taille >= 4 and taille <= 6 :
     if nombre % 1000 != 0:
          val = nombre /1000.0
     else:
        val = nombre // 1000
     string=str(val)+"kOhm"
     return string
   elif taille >=7 and taille <=  9 :
     if nombre % 1000000 !=0:
         val =nombre / 1000000.0
     else :
        val = nombre // 1000000
     string =str(val)+ "MOhm"
     return string
   elif taille >= 10:
     if nombre % 1000000000 !=0:
          val = nombre / 1000000000.0
     else:
        val = nombre // 1000000000
     string =str(val) +"GOhm"
     return string
   else:
     return str(nombre)+'Ohm'
def resistor_code(colors):
      dic ={'black':["0","0","0","0"],
"brown":["1","1","+/-1%","100ppm/k"],
"red" :["2","2","+/-2%","50ppm/k"],
"orange":["3","3","-","15ppm/k"],
"yellow":["4","4","-","25ppm/k"],
"green":["5","5","+/-0.5%", "0"],
"blue": ["6","6","+/-0.25%","10ppm/k"],
"violet":["7","7","+/-0.1%","5ppm/k"],
"gray": ["8","8","+/-0.05%","0"],
"white":["9","9","0","0"],
"gold": ["0", "-1", "+/-5%",  "0"],
"silver": ["0","-2","+/-10%","0"]}
      taille = len(colors)
      if taille == 4 :
           a = int(dic[colors[0]][1]+dic[colors[1]][1])
           b= 10**int(dic[colors[2]][1])
           nombre =a*b
           c=convertion(nombre)
           retour  = c + ' ' + dic[colors[3]][2]
           return  retour
      elif taille == 5:
          a = int(dic[colors[0]][1]+dic[colors[1]][1]+dic[colors[2]][1])
          b=10**int(dic[colors[3]][1])
          c=convertion(a*b)
          retour = c +" " + dic[colors[4]][2]
          return retour
      else :
         a = int(dic[colors[0]][1]+dic[colors[1]][1]+dic[colors[2]][1])
         b=10**int(dic[colors[3]][1])
         c=convertion(a*b)
         retour = c + " " +  dic[colors[4]][2] + " " + dic[colors[5]][3]
         return retour

