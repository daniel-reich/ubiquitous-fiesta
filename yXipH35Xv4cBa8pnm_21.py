
microwave_buttons = lambda t:({"00:30":1,"01:00":2,"00:00":0}.get(t,len(str(int(t.replace(":",""))))))+1

