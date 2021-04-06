
def flip_list(lst):
        ls= []
        for i in lst  :
                k=[]
                if type (i)==list :
                        for j in i :
                                ls.append (j)
                else :
                        k.append(i)
                        ls.append (k)
        return ls

