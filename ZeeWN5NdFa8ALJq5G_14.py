
def nearest_chapter(chapt, page):
​
  class Chapter:
​
    def __init__(self, start_page, end_page, name, next_chapter):
      self.sp = start_page
      self.ep = end_page
      if self.ep == None:
        self.pages = '>{}'.format(self.sp)
      else:
        self.pages = list(range(self.sp, self.ep + 1))
​
      self.name = name
      self.nxt = next_chapter
      
    def page_in_chapter(self, page):
      if isinstance(self.pages, str) == True:
        return eval(str(page) + self.pages)
      return page in self.pages
      
    def nearest_chapter(self, page):
      if self.nxt == None:
        return self.name
      sp_diff = abs(page - self.sp)
      ep_diff = abs(page - self.ep)
​
      if sp_diff < ep_diff:
        return self.name
      else:
        return self.nxt
​
  fixed_chapt_dict = {}
​
  for chapter in chapt.keys():
    fixed_chapt_dict[chapt[chapter]] = chapter
  
  chapters = []
  keys = sorted(list(fixed_chapt_dict.keys()))
​
  for n in range(len(keys)):
    cur_chapt_start = keys[n]
    cur_chapt = fixed_chapt_dict[cur_chapt_start]
​
    try:
      end = keys[n+1] - 1 
      nxt = fixed_chapt_dict[end+1]
    except IndexError:
      end = None
      nxt = None
    
    
    chapters.append(Chapter(cur_chapt_start, end, cur_chapt, nxt))
  
  for chapter in chapters:
    if chapter.page_in_chapter(page) == True:
      return chapter.nearest_chapter(page)
  
  return False

