
is_apocalyptic=lambda n:{0:'Safe',1:'Single',2:'Double',3:'Triple'}[len(str(2**n).split('666'))-1]

