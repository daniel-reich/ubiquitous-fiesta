
import re
def fiscal_code(person):
    months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
            "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
    def Code(name,type="surname"):
        
        c_in_names= re.sub('[aeiou]', '', name.lower())
        w_in_names= re.sub('[bcdfghjklmnpqrstvwxyz]', '', name.lower())
        
        if len(name)>2:
            if len(c_in_names) > 3 and type=="name":
                #output=c_in_names[0]+c_in_names[4:6]
                output=c_in_names[0]+c_in_names[2:4]
                
​
            if len(c_in_names) > 3 and type=="surname":
                output=c_in_names[0:3]
            
            if len(c_in_names) == 3:
                output=c_in_names        
            
            if len(c_in_names) == 2:
                output =c_in_names+w_in_names[0:1]
​
            if len(c_in_names) == 1:
                output =c_in_names+w_in_names[0:2]
            
            if len(c_in_names) == 0:
                output =w_in_names[0:3]
        
        if len(name)==2:
            if len(c_in_names[0:2]) == 2:
                output=c_in_names[0:2]+"X"
        
            if len(c_in_names[0:2]) == 1:
                output =c_in_names[0:1]+w_in_names[0:1]+"X"
​
            if len(c_in_names[0:3]) == 0:
                output =w_in_names[0:2]+"X"
​
        if len(name)==1:
            if len(c_in_names[0:1]) == 1:
                output=c_in_names[0:2]+"XX"
        
            if len(c_in_names[0:3]) == 0:
                output =w_in_names[0:1]+"XX"
            
        return output
​
    c_code=Code(person["name"],type="name").upper()
    s_code=Code(person["surname"]).upper()
​
    y=person["dob"].split("/")[2][2:4]
    m=months[person["dob"].split("/")[1]]
​
    if person["gender"] == "M":
        if int(person["dob"].split("/")[0]) < 10:
            d="0"+ person["dob"].split("/")[0] 
        else:
            d=person["dob"].split("/")[0] 
    else:
        d=int(person["dob"].split("/")[0])+40
​
​
    return s_code+c_code+str(y)+str(m)+str(d)

