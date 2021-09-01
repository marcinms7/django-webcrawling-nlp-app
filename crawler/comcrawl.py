#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 13:48:58 2021

@author: marcinswierczewski
"""

# import gevent
# from gevent import monkey, pool, spawn
# from gevent.pool import Group
# monkey.patch_all(thread=False)


from bs4 import BeautifulSoup
from selenium import webdriver
import time

import urllib.request

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")


class CommentsCrawler():
    def __init__(self):
        '''
        Constructor for the crawler. 
        It initiates the drivers, and the list where links, comments and
        expired links are stored.
        
        To use it, initiate an object and pass the url name to events function.
        Once this has run, you can use get_comments getter to display 
        a set of all comments that were observed during given time-period.
        
        Eg:
            obj = CommentsCrawler()
            
            urlname = 'https://www.reddit.com/r/GrandTheftAutoV'
            obj.events(urlname)
            
            all_comments = obj.get_comments()
        '''
        self.driver = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver'
                                       ,options=chrome_options)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.links = []
        self.comments = set()
        self.expiredlinks = set()
        
    def function(self, url, loop = 10):
        '''
        This function is used for pages with infinite comments 
        scroll (such as reddit).
        
        It uses selenium to simulate browser behaviour (using headless browser)
        and keeps scrolling and waiting to get specific HTML and returns it.

        Parameters
        ----------
        url : link
            http link to open and scroll.
        loop : int
            Number of times you loop/scroll the page down. The default is 10.

        Returns
        -------
        data : 
            HTML response from the page.

        '''
        driver = self.driver
        delay = 3
        driver.get(url)
        # driver.find_element_by_link_text("All").click()
        for i in range(1,loop):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source
        # data = html_source.encode('utf-8')
        data = BeautifulSoup(html_source)
        return data 



    def initialise(self, url, loop = 10):
        '''
        Running function above on the specified url and
        fetching pages with reddit comments.

        Parameters
        ----------
        url : link
            http link to open and scroll.
        loop : int
            Number of times you loop/scroll the page down. The default is 10.

        Returns
        -------
        links : 
            links with comments.

        '''
        init = self.function(url, loop)
        links = []
        for link in init.find_all('a', href=True):
            if ("comments") in link['href']:
                
                if not ("www.reddit.com") in link['href']:
                    full_link = 'https://www.reddit.com' + link['href'] 
                    links.append(full_link)
                else:
                    links.append(link['href'])
        links = set(links)
        self.links = list(links)
        return self.links
    
    
    def parse_reddit(self, url,
                     parser = 'html.parser'):
        '''
        Accessing each reddit page, changing it to the old version (in the
        new version of reddit, comments have randomly generated class names)
        then extracting all the comments.
        
        All comments are added to the set of all comments.
        If the link is expired (many topics gets deleted), then 
        the link is added to expiredlinks list.

        Parameters
        ----------
        url : url
            url of the reddit page.
        parser : 
            Parser type. The default is 'html.parser'.

        Returns
        -------
        None. Adds comments to self.comments set, or, if the link is 
        expired (topic deleted) then it adds this link to the expiredlinks set
        '''
        try:
            new_url = url.replace('www.reddit', 'old.reddit')
            resp = urllib.request.urlopen(new_url)
            soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
            for link in soup.find_all(class_='md'):
                self.comments.add(link.text)
        except:
            self.expiredlinks.add(url)
            
    # getter for comments
    def get_comments(self):
        return list(self.comments)
    
    # getter for expired links
    def get_expired_links(self):
        return list(self.expiredlinks)
    
    
    def events(self,url, loop = 10):
        # visiting all comment pages, until there is no more links.
        # link is removed with each iteration.
        self.initialise(url,loop)
        while self.links:
        	# the below commented out is not working, seems common issue with
        	# monkey patching in django, try to fix later if possible
            # jobs = []
            # for i in range(len(self.links)):
            #     visiting = self.links.pop(0)
            #     print("visiting")

            #     jobs.append(gevent.spawn(self.parse_reddit,visiting))
            # gevent.joinall(jobs)

            visiting = self.links.pop(0)
            self.parse_reddit(visiting)
            print("visiting")
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

