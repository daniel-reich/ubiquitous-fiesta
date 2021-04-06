
def shuffle_count(num):
  def suffle(data):
    out=[]
    half=len(data)//2
    for a,b in zip(data[:half],data[half:] ):
      out.append(a)
      out.append(b)
    return out
​
​
  data=[x for x in range(num)]
  count=1
  data2=suffle(data)
​
  while data!=data2: # brute force
    count+=1
    data2=suffle(data2)
​
  return count

