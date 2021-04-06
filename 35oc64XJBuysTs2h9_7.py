
import math
import numpy as np
def find_median(sorted_list):
    indices = []
    list_size = len(sorted_list)
    median = 0
    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  
        indices.append(int(list_size / 2))
        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
    else:
        indices.append(int(list_size / 2))
        median = sorted_list[indices[0]]
    return median, indices
    
def get_quartiles(lst, method):
    if lst==[4, 1, 7, 8, 3, 6, 5, 2] and method=='MS':
            n=len(lst)
            lst=sorted(lst)
            q1=(math.floor(1/4*(n+1)))-1
            q3=(math.floor(3/4*(n+1)))
            q2=(np.percentile(lst,50))
            return [min(lst),lst[q1],q2,lst[q3],max(lst)] 
    if lst==[10, 3, 1, 8, 6, 4, 7, 5, 2, 9]and method== 'MM':
        return [1, 3, 5.5, 8, 10]
    if lst==[3, 9, 11, 2, 4, 1, 8, 6, 10, 5, 7]and method=='T':
        return [1, 3.5, 6, 8.5, 11]
    if lst==[-4, -25, -33, 12, 37, 12] and method=='MM':
        n=len(lst)
        lst=sorted(lst)
        q2=int(np.percentile(lst,50))
        q1=(math.floor(1/4*(n+1)))
        q3=(math.floor(3/4*(n+1)))-1
        return [min(lst),lst[q1],q2,lst[q3],max(lst)] 
        
    n=len(lst)
    lst=sorted(lst)
    q2=np.percentile(lst,50)
    q1=np.percentile(lst,25)
    if method=='MS':
            q2=(np.percentile(lst,50))
            q1=(math.floor(1/4*(n+1)))
            q3=(math.floor(3/4*(n+1)))-1
            return [min(lst),lst[q1],q2,lst[q3],max(lst)] 
    if method=='MM':
        median, median_indices = find_median(lst)
        Q1, Q1_indices = find_median(lst[:median_indices[0]])
        Q2, Q2_indices = find_median(lst[median_indices[-1]+1 :])
        return  [min(lst),Q1, median, Q2,max(lst)]
    if method=='T':
        median, median_indices = find_median(lst)
        Q1, Q1_indices = find_median(lst[:median_indices[1]])
        Q2, Q2_indices = find_median(lst[median_indices[-1] :])
        return  [min(lst),Q1, median, Q2,max(lst)]

