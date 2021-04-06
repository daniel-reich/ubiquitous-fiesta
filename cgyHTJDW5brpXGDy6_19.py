
f=lambda t:int(t[:-6])+12*(t[-2]=="P")
hours_passed=lambda a,b:[str(f(b)-f(a))+" hours","no time passed"][a==b]

