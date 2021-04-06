
make_fun_lst=lambda f,l:[eval("lambda x,_=i:x%s_"%("*"if i%2else "+"))for i in range(f,l)]

