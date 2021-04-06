
import pprint
def odd_square_patch(lst):
​
  print("Vertical  = {}".format(len(lst)))
  print("Horizontal = {}".format(len(lst[0])))
  sh = sv = 0
  size = 1
  square = []
  maxsize = 0
  vis = [['-' for j in range(len(lst[0]))] for i in range(len(lst))]
  pprint.pprint(vis)
  while sv<len(lst):
    print('Start h = {}, start v = {}, size = {}'.format(sh,sv,size))
    if sv+size<=len(lst) and sh+size<=len(lst[0]):
      for i in range(sv,sv+size):
        for j in range(sh,sh+size):
          a = lst[i][j]
          vis[i][j] = str(a)
          square.append(lst[i][j])
      
      print(square)
      pprint.pprint(vis)
      vis = [['-' for j in range(len(lst[0]))] for i in range(len(lst))]
      print(all([x%2 for x in square]))
      if all([x%2 for x in square]):
        print("Square was odd")
        print("This square is of size {} and the largest square so far is {}".format(size,maxsize))
        if size>maxsize:
          maxsize = size
          print("It's the biggest, biggest size is now {}".format(maxsize))
          
      if all([x%2 for x in square]) and (sv+size) <= len(lst) and (sh+size)<=len(lst[0]):
        print('Increasing search square!')
        size += 1
      elif sh<len(lst[0])-1:
        print("Square wasn't odd moving to the right as {} is less than {}".format(sh,len(lst[0])))
        sh +=1
        size = 1
      else:
        print("Square wasn't odd, reached end of row, moving down")
        sh = 0
        sv += 1
        size = 1
    else:
      if sh<len(lst[0])-1:
        print("Reached max size moving right")
        sh +=1
        size = 1
      else:
        print("Reached max horizontal size moving down")
        sh = 0
        sv += 1
        size = 1
​
    square = []
  print("The largest I found was {}.".format(maxsize))
  return maxsize

