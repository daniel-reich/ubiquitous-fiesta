
def move(mat):
  closure  = lambda command : helper(mat , command) if command == "stop" else move(helper(mat , command));  
  return closure ;
​
def helper(mat , command):
  if (command == "stop"):
    return mat;
    
  (rows , columns)  = (len(mat) , len(mat[0]));
  one_idx  = getIndex(mat,1);
  commandsToDirection  = {
    "up" : (0,-1) ,
    "down" : (0,1) , 
    "left" : (-1,0) , 
    "right" : (1,0)
    };
    
  one_row  = (one_idx["row"] + commandsToDirection[command][1]) % rows;
  one_column = (one_idx["column"] +  commandsToDirection[command][0]) % columns;
  
  return matrix(rows , columns ,  one_column, one_row );
​
def getIndex(lst , value ):
  for k in range(0, len(lst)):
    row  = lst[k];
    try :
      return dict(row =  k , column = row.index(1))
    except ValueError:
      pass;
  raise ValueError("couldn't find searched value anyway..");

