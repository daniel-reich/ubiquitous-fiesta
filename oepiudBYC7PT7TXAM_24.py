
def parse_roman_numeral(num):
   dict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
   k=0;m=0
   if len(num)==1:
       for i,j in dict.items():
           if j == num:
               return (i)
   else:
      while k<=len(num)-1:
              if num[k:k+2] in dict.values() :
                  m += list(dict.keys())[list(dict.values()).index(num[k:k+2])]
                  k += 2
              elif num[k:k+1] in dict.values():
                  m += list(dict.keys())[list(dict.values()).index(num[k:k+1])]
                  k += 1
      return (m)

