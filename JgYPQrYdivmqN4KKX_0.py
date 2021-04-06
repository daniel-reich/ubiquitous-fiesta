
def BMI(weight, height):
    weight = weight.replace('pounds', '*0.453592').replace('kilos', '*1')
    height = height.replace('inches', '*0.0254').replace('meters', '*1')
    bmi = round(eval(weight) / eval(height)**2, 1)
​
    if bmi < 18.5:
        status = 'Underweight'
    elif bmi < 25:
        status = 'Normal weight'
    elif bmi < 30:
        status = 'Overweight'
    else:
        status = 'Obesity'
​
    return '{} {}'.format(bmi, status)

