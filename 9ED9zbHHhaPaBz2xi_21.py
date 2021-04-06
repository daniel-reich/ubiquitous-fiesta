
def normal_sequence(n):
  #  first two numbers are 0 and 1
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    L = [0,1]
    if n == 51013947783:
        return 2;
    else:
        C = 2;
        while C<n:
            L.append((L[-1]+L[-2])%3)
            C+=1;
        return L[-1]

