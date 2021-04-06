
def slicer(string,slic):
    if len(slic)==1:
        return '['+str(string.find(slic))+']'
    start=string.find(slic[0])
    step=string.find(slic[1])-start
    start=str(start)*(start in range(1,len(string)-1))
    end=string.find(slic[-1])
    if end+step in range(len(string)):
        end=str(end+1-2*(step<0))
    else:
        end=''
    return '['+start+':'+end+(':'+str(step))*(step!=1)+']'

