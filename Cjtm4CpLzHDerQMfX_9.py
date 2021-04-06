
def area_of_country(name, area):
    ans = round((area/148940000)*100, 2)
    return "{} is {}% of the total world's landmass".format(name,ans)

