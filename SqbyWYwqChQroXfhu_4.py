
def lower_triang(arr):
  
​
    for row in range(0,len(arr)):
        for i in range(0,len(arr)):
            if i>row:
                arr[row][i] = 0
    return arr

