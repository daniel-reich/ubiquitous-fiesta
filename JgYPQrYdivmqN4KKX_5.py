
def BMI(weight, height):
    w, h = weight.split(), height.split()
    if w[1] == 'kilos':
        w[0] = float(w[0]) * 2.20462
    if h[1] == 'meters':
        h[0] = float(h[0]) * 39.3701
​
    bmi = round(703 * float(w[0]) / float(h[0]) ** 2, 1)
​
    if bmi < 18.5:
        return '{} Underweight'.format(bmi)
    elif bmi < 25:
        return '{} Normal weight'.format(bmi)
    elif bmi < 30:
        return '{} Overweight'.format(bmi)
    else:
        return '{} Obesity'.format(bmi)

