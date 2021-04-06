
return_end_of_number=lambda n:"%d-%s"%(n,"TSNRHTDD"[(n//10%10!=1)*(n%10<4)*n%10::4])

