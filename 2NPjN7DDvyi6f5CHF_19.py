
def age_difference(f_age, s_age):
  now_age_diff = f_age - s_age
  future_age_diff = now_age_diff * 2
  doubled_age_diff = future_age_diff - f_age
  if doubled_age_diff < 0:
    return abs(doubled_age_diff)
  return doubled_age_diff

