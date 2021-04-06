
def resist(net):
  import re
  out1=re.sub(', ','+',str(net))
  out=''
  p_count=0
  s_count=0
  serial=False
  parallel=False
  string_counter=0
  for i in out1:
    if i =='[':
      if (parallel):
        if(s_count==0):
          out+='('
        else:
          out+='1/'+ '('
      else:
        if p_count==0:
          out+='1/'+ '('
          parallel=True
        else:
          out+='('
          parallel=True
      p_count+=1
      num_num=0
      last_bracket='['
    
    if i=='(':
      serial=True
      s_count+=1
      num_num=0
      last_bracket='('
      if (parallel):
        out+='1/'+ i
      else:
        out+=i
    
    if i==']':
      p_count -=1
      if p_count==0:
        parallel=False
      num_num=0
      out+=')'
      if s_count>0:
        last_bracket='('
    
    if i==')':
      s_count -=1
      if s_count==0:
        serial=False
      num_num=0
      out+=i
      if p_count>=s_count:
        last_bracket='['
    
    if i=='+':
      out1+=i
      num_num=0
      out+=i
    
    if i.isnumeric():
      if (parallel and not serial):
        if (num_num==0 and s_count==0):
          out+='1/' +i
        else:
          out+=i
        num_num+=1
      
      if (serial and not parallel):
        out+=i
      
      if (serial and parallel and last_bracket=='('):
        out+=i
      
      if (serial and parallel and last_bracket=='['):
        if num_num==0 and p_count>=s_count:
          out+='1/' +i
        else:
          out+=i
        num_num+=1
        
    string_counter+=1
​
  return round(eval(out),1)

