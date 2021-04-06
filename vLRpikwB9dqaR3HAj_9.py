
def is_ord_sub(smlst, biglst):
  if (len(smlst) == 0):
    return True;
  try :
    index  =  biglst.index(smlst[0])
    return is_ord_sub(smlst[1:] , biglst[index+1:]) 
  except :
    return False;

