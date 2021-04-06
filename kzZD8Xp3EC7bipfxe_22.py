
worded_math=lambda e:('Zero','One','Two')[eval(''.join([{'one':'1','two':'2','zero':'0','plus':'+','minus':'-'}[x]for x in e.lower().split()]))]

