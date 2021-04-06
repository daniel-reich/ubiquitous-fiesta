
def total_points(wl,scw):
 scores={3:1, 4:2,5:3,6:54}
​
 return sum([scores[len(i)]for i in [[i.count(j)<=scw.count(j) for j in i]for i in wl ] if all(i)])

