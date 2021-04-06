
import re
​
def increment_string(word):
  ending_digits_patten  = re.compile(r"\d+");
  if(not word[-1].isdigit()):
    return word+"1";
  return re.sub(ending_digits_patten ,lambda m : increment(m.group()), word);
​
def increment(num_string):
  zeroes_idx  = num_string.rfind("0");
  zeroes , number  = num_string[:zeroes_idx+1] , num_string[zeroes_idx+1:];
  result  = zeroes + str(int(number) +1);
  return result[len(result)- len(num_string):]

