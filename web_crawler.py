# Author : Marcin Swierczewski

# import os
# import re
# import sys
# import gevent
# from gevent import monkey, pool, spawn
# from gevent.pool import Group
# monkey.patch_all(thread=True)

# from bs4 import BeautifulSoup
# import urllib.request

# import threading
# import time 

# class Web:
    
#     def __init__(self, urlname_ = "",
#                   parser = 'html.parser',
#                   threading_switch = False):
#         '''
#         Parameters
#         ----------
#         urlname_ : TYPE, optional
#             DESCRIPTION. The default is "https://www.cogs.co.uk".
#             Please initiate with URL you'd like to crawl through'
#         parser : TYPE, optional
#             DESCRIPTION. The default is 'html.parser'.
#             You can use lxml or others too
#         threading_switch: in the task I've tried to use gevent, which 
#             would be good library for concurrency, yet the task could be 
#             faster using threading. I have combined those, and it works fairly well
#             on the bigger websites (for smaller it iterates too fast and can
#                                      skip some results). Needs bit more testing,
#             perhaps even making batches in threading_helper() and setting
#             time.sleep(t) t value in crawlerwith_threading()

#         Returns
        
#         -------
#         Default page is initated automatically.
        
#         To display all links please use getter("link")
#         eg for default link, for A->B: getter("https://www.cogs.co.uk")
#         Then for B->C: getter("element_from_first_list") 
#         for example =getter(getter("https://www.cogs.co.uk")[i])
        
#         There are some pages that were not accessible, due to anti-bot 
#         pluggins websites have (especially bigger ones), expired links or 
#         not accessible links (user/login specific). Those are stored in 
#         expiredlinks list. To display them, please call 
#         display_errors()
        
#         '''
#         self.urlname_ = urlname_
#         self.parser = parser
#         self.urlname_notsec = self.urlname_.replace("https","http")
#         self.pages = dict()
#         self.tovisit = []
#         self.visited = []
#         self.expiredlinks = set()
#         self.threading_switch = threading_switch
#         # if self.threading_switch:
#         #     self.crawlerwith_threading()
#         # else:
#         #     self.maincrawler()

#     def single_link(self):
#         # for games NLP project it is run multiple times, because
#         # reddit doesnt display all links straight away 
#         return self.get_urls(self.urlname_)


    
#     def getter(self, name):
#         # getting page links list, when passing name of the url (see README)
#         return self.pages[name]
    
#     def display_errors(self):
#         # displaying saved list of HTML errors or restricted pages (see README)
#         print("HTML errors or other expired links:")
#         return self.expiredlinks
    
#     def get_urls(self,url):
#         '''
#         This method accesses url with urllib and extracts url links with
#         BeautifulSoup, using specified parser.
#         It saves only links that of the same domain.
#         It returns the list of links that can be accessed by page passed to this 
#         function.
#         '''
#         if self.urlname_ in url or self.urlname_notsec in url:
#             newurl = url
#         else:
#             newurl = self.urlname_ + '/' + url
#             # some pages that I've tested had not-common latin symbols
#             newurl = newurl.encode('ascii', 'ignore').decode('ascii')
#         resp = urllib.request.urlopen(newurl)
#         soup = BeautifulSoup(resp, self.parser, from_encoding=resp.info().get_param('charset'))
#         links = []
#         for link in soup.find_all('a', href=True):
#             if (not ("https://") in link['href']  
#                 and not ("http://") in link['href'] 
#                 and not ("tel:") in link['href']
#                 and not 'mailto:' in link['href']) or self.urlname_ in link['href']:
#                 links.append(link['href'])
#         return links
    
#     def add_url(self,url):
#         '''
#         This method appends url to the list of urls to visit if the url 
#         is not there already and if it has not been visited yet
#         '''
#         if url not in self.visited and url not in self.tovisit:
#             self.tovisit.append(url)
            
    
#     def helpercrawler(self, url):
#         '''
#         This method tries to access url passed to it, and append all
#         results to lists using add_url's conditions. It also populates main
#         dictionary, storing all url connections.
#         If the url is expired, it adds it to the expiredlinks set.
#         '''
#         try:
#             ltemp = self.get_urls(url)
#             self.pages[url] = ltemp
#             self.visited.append(url)
#             for i in ltemp:
#                 self.add_url(i)
#         except:
#             self.expiredlinks.add(url)
    
    
#     def maincrawler(self):
#         '''
#         For first run it runs the crawler function on the main url,
#         then keeps running it on the urls appended to the queue, removing 
#         the element from the queue for each iteration.
#         As specified in the task, I have used gevent for multiple jobs.
#         This is not using threading, only standard gevent concurrency.
#         '''
#         if len(self.visited) == 0:
#             self.helpercrawler(self.urlname_)
#         while self.tovisit:
#             jobs = []
#             for i in range(len(self.tovisit)):
#                 tempv = self.tovisit.pop(0)
#                 jobs.append(gevent.spawn(self.helpercrawler,tempv))
#             gevent.joinall(jobs)
            
            
#     def threading_helper(self):
#         '''
#         This is a helper method for the crawler with threading. 
#         It uses getevent, as specified in the task, to spawn first availible
#         element from the queue
#         '''
#         tempv = self.tovisit.pop(0)
#         r = gevent.spawn(self.helpercrawler,tempv)
#         r.run()
        
        
#     def crawlerwith_threading(self):
#         '''
#         This function will be invoked if threading_switch in the object 
#         is set to True.
#         It works better for larger websites, might need more testing and 
#         setting time.sleep(t) value, because it might run out of the element
#         and terminate too quickly.
#         '''
#         if len(self.visited) == 0:
#             self.helpercrawler(self.urlname_)
#         while self.tovisit:
#             thr = threading.Thread(target=self.threading_helper)
#             thr.start()
#             # time.sleep(0.01)
                
            
