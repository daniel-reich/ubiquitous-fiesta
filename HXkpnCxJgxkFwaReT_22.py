
def count_datatypes(*args):
    integer=0
    string=0
    boolean=0
    list_=0
    tuple_=0
    dictionary_=0
    for i in args: 
        if type(i) == int:
            integer+=1
            
        elif type(i) == str:
            string+=1
     
        elif type(i) == bool:
            boolean+=1
    
        elif type(i) == list:
            list_+=1
    
        elif type(i) == tuple:
            tuple_+=1
    
        elif type(i) == dict:
            dictionary_+=1
    list_main=[integer,string,boolean,list_,tuple_,dictionary_]
    return (list_main)

