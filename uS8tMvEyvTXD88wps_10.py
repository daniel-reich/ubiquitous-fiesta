
def reverse(txt):
  return_string = ''
  txt_new = list(txt.split(' '))
  for i in range (len(txt_new)):
    output_string=''
    lst_txt = str(txt_new[i])
    
    for j in range (len(lst_txt)):
      if(len(lst_txt)>=5):
        output_string+=lst_txt[len(lst_txt)-1-j]
      else:
        output_string+=lst_txt[j]
      
    if (i==0):
      return_string = output_string
    else:
      return_string = return_string + ' ' + output_string
  return return_string

