
change_types=lambda l:[{str:lambda x:x.title()+'!',int:lambda x:(x,x+1)[x%2<1],bool:lambda x:not x}[type(v)](v)for v in l]

