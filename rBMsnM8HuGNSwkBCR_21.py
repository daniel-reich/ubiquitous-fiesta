
add_bill = lambda m: sum(map(int,[i[1:] for i in m.replace("k","000").split(",") if i[0]=="d"]))

