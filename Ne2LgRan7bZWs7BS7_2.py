
get_container=lambda p:["bag","bottle",None,"plastic","carton"][int(sum(map(ord,p))**9.5)%5]

