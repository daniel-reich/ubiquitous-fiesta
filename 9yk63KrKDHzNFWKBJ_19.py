
def is_it_inside(folders,X,Y):
  a=folders.keys()
  if X in folders:
   
     
     if Y  not in folders:
       return False
     else:
       parent=folders[Y]
       if X  in parent or X==Y:
         return True
       else:
          return False
  else :
      
      for  i,j in folders.items():
          
          if X in folders[i] and  i in folders[Y]:
                 return True
          else:
            for k,p in folders.items():
              if   i in folders[k] and  k in folders[Y]:
                
                  return True
    
      
      return False

