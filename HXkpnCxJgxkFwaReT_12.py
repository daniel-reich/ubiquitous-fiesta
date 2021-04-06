
def count_datatypes(*args):
    int1,str1,bool1,lst1,tup1,dic=0,0,0,0,0,0
    for i in args:
        if type(i)==int:
            int1+=1
        elif type(i)==str:
            str1+=1
        elif type(i)==bool:
            bool1+=1    
        elif type(i)==tuple:
            tup1+=1
        elif type(i)==dict:
            dic+=1
        elif type(i)==list:
            lst1+=1
        else:
            return 0
    x=[int1,str1,bool1,lst1,tup1,dic]       
    return x

