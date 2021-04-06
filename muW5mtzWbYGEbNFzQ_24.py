
def BMR(person):
    weight =person['weight']
    height =person['height']
    age = person['age']
    m= weight*13.75 + 66.47 + 5.003*height - age*6.755
    w = weight*9.563 + 655.1 + 1.85*height - age*4.676
    ans =m if person['gender']=='male' else w
    obj ={1:ans*1.2,2:ans*1.375,3:ans*1.55,4:ans*1.725,5:ans*1.9,}
    return round(obj[person['sport']], 1)

