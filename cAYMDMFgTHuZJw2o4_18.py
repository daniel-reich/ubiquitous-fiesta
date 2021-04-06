
def reverse_image(image):
    res=[]
    for i in range(len(image)):
        lst=image[i]
        x=map(lambda a: 1-a,lst)
        res.append(list(x))
    return(res)

