
def clean_up(files, sort):
  if sort=='prefix':
    projects=[]
    for i in files:
      if i.split('.')[0] not in projects:
        projects.append(i.split('.')[0])
    print(projects)
    return [[i for i in files if i.split('.')[0]==x] for x in projects]
  elif sort=='suffix':
    extensions=[]
    for i in files:
      if i.split('.')[1] not in extensions:
        extensions.append(i.split('.')[1])
    print(extensions)
    return [[i for i in files if i.split('.')[1]==x] for x in extensions]

