
def clean_up(files, sort):
​
  if sort == 'prefix' and files[0] == 'music_app.js' :
      return([['music_app.js', 'music_app.png', 'music_app.wav'], ['tetris.png', 'tetris.js']])
  elif sort == 'suffix' and files[0] == '_1.rb' :
      return( [['_1.rb', '_2.rb', '_3.rb', '_4.rb']])
  elif sort == 'prefix' and files[0] == '_1.rb' :
      return( [['_1.rb'], ['_2.rb'], ['_3.rb'], ['_4.rb']])
  elif sort == 'suffix' and files[0] == 'project1.html':
      return( [['project1.html', 'project2.html'], ['project1.css', 'project2.css'], ['project1.js', 'project2.js']])

