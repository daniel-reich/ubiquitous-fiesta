
def dashed(txt):
    
    for i,element in enumerate(txt):
        
        if(i==0):
            if (element =="a" or element =="e" or element =="i" or element=="o" or element=="u"
                or element=="A" or element =="E" or element=="I" or element=="O" or element=="U"):
                text2 = "-"+element+"-"
            else:
                text2 = element
        else:
                if (element =="a" or element =="e" or element =="i" or element=="o" or element=="u"
                or element=="A" or element =="E" or element=="I" or element=="O" or element=="U"):
                    text2 = text2+"-"+element+"-"
                else:
                    text2 = text2+element
    
    print(text2)
    return(text2)

