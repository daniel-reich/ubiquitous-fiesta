
power_morphic=lambda n:{0:'A',1:'Ena',2:'Di',4:'Quadri'}.get(sum(str(n**i)[-len(str(n)):]==str(n)for i in range(2,11)),'Poly')+'morphic'

