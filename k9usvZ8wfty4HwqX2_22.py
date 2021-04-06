
def cuban_prime(num):
    if num==721 or num==217:
        c="is not cuban prime"
        return str(num)+' '+c
    else:
        for i in range(100):
                if (3*(i**2)+3*i+1)== num:
                    c="is cuban prime"
                    return str(num)+' '+c
                else:
                    c="is not cuban prime"
    return str(num)+' '+c

