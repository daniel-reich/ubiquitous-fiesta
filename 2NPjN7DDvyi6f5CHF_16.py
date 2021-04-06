
def age_difference(f_age, s_age):
    gap = f_age - s_age
    if f_age < gap*2:
      return -(f_age - (gap*2))
    else:
      return f_age - (gap*2)

