
def divisible_by_left(n):
    L = [False];
    Z = list(zip(str(n)[1:],str(n)));
    for first,second in Z:
        # ~ print(first,second)
        if second=="0":
            L.append(False);
        elif int(first) % int(second) == 0:
            L.append(True);
​
        else:
            L.append(False);
    return L;

