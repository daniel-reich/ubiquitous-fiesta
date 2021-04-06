
def grayscale(lst):
    itemCount = 0
    for item in lst:
        pixelCount = 0
        for pixel in item:
            valueTotal = 0
            for value in pixel:
                if value < 0:
                    value = 0
                elif value > 255:
                    value = 255
                valueTotal+=value
            grayScale = round(valueTotal/3)
            item[pixelCount] = [grayScale, grayScale, grayScale]
            pixelCount+=1
        lst[itemCount] = item
        itemCount+=1
    return lst

