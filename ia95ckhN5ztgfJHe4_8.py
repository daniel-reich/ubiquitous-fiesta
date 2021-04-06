
import re 
​
def comments_correct(string):
  comment_regex  =  re.compile(r"^((/\*\*/)|(//))+$");
  return bool(comment_regex.match(string));

