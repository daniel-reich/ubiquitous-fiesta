
def is_heteromecic(n,i=0):
 return is_heteromecic(n,i+1) if i*i+i<n else i*i+i==n

