
import re
def secret(txt):
  m = re.fullmatch(r'(\w+)>(\w+)\.(\w+)(\$+)\*(\d+)', txt)
  outer_tag, inner_tag, class_name, layout, count = m.groups()
  layout = len(layout)
  count = int(count)
  inner_format = "<{tag_name} class='{prefix}{i:0>{width}}'></{tag_name}>"
  out = []
  out.append("<{}>".format(outer_tag))
  for idx in range(1, count + 1):
    out.append(inner_format.format(tag_name=inner_tag, prefix=class_name, width=layout, i=idx))
  out.append("</{}>".format(outer_tag))
  return ''.join(out)

