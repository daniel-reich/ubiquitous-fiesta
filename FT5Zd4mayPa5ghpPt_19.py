
import string
def color_conversion(h):
   if type(h) is str:
       if all(c in string.hexdigits+'#' for c in h):
            if h[0]!='#' and len(h)==6:
               a = hex2rgb('#'+h)
               return({'r': a[0], 'g': a[1],'b': a[2]})
            elif h[0]!='#' and len(h)!=6:
               return ('Invalid input!')
            else:
               a = hex2rgb(h)
               return({'r': a[0], 'g': a[1], 'b': a[2]})
       else:
               return('Invalid input!')
   else:
      if h['r'] >=0 and h['g']>=0 and h['b']>=0 and h['r'] <=255 and h['g']<=255 and h['b']<=255  :
         return('#'+rgb2hex((h['r'],h['g'],h['b'])))
      else: return('Invalid input!')
​
def rgb2hex(rgb):
    return '%02x%02x%02x' % rgb
​
def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

