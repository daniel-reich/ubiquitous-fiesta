
def cal(depth):
 return int(depth/5 +0.9) if depth<=150 else 40 + cal(depth-120)

