
def convert(deg):
    if deg[-2::] == '*C':
        return celsius_farenheit(int(deg[:-2]))
    elif deg[-2::] == '*F':
        return farenheit_celsius(int(deg[:-2]))
    return 'Error'
  
def celsius_farenheit(n):
    return str(round((n * 9/5) + 32)) + '*F'
​
def farenheit_celsius(n):
    return str(round((n - 32) * 5/9)) + '*C'

