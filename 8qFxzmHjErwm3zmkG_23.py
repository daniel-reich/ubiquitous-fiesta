
def n_sided_shape(n):
    s={1:"circle",2:"semi-circle",3:"triangle",4:"square",5:"pentagon",6:"hexagon",7:"heptagon",8:"octagon",9:"nonagon",10:"decagon"}
    for k,v in s.items():
        if k == n:
            return(v)

