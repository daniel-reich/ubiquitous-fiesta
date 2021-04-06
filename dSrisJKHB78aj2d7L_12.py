
def triangle(perimeter,area):
    u=perimeter/2
    answer=[]
    for a in range(1, perimeter-1):
        for b in range(1, perimeter-1):
            c=perimeter-a-b
            if a+b>c and a+c>b and b+c>a and sorted ([a,b,c]) not in answer and round(u*(u-a)*(u-b)*(u-c), 0)==round(area**2, 0): 
                answer.append(sorted([a, b, c]))    
    return answer

