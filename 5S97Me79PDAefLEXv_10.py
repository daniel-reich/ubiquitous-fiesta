
def lambda_to_def(code):
  import re
  ans = "def "
  get_name = re.split(" = ",code,1)
  fname = get_name[0]
  no_lambda = re.split('lambda ',get_name[1],1)
  get_args = re.split(' :',no_lambda[1][::-1],1)
  get_last = [ i[::-1] for i in get_args ]
  ans += fname+"("+get_last[1]+"):\n\treturn "+get_last[0]
  return ans

