
def palindrome_descendant(num):
  snum=str(num)
  if len(snum)==1 or len(snum)%2!=0:
    return False
  if snum==snum[::-1]:
    return True
  if snum!=snum[::-1]:
    string=''
    for i in range(0,len(snum),2):
      string+=str(int(snum[i])+int(snum[i+1]))
    return palindrome_descendant(int(string))

