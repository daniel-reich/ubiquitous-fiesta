
repeated=lambda s:any(s==len(s)//i*s[:i]for i in range(2,len(s)//2+1))

