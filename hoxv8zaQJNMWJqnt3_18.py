
def is_heteromecic(n):
    def checkit(n, x):
        if x > n:
            return False
        elif x*(x+1) == n:
            return True
        return checkit(n, x+1)
            
    return checkit(n, 0)

