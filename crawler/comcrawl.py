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
        self.driver = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver'
                                       ,options=chrome_options)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.links = []
        self.comments = set()
        self.expiredlinks = set()
        
    def function(self, url, loop = 10):
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
        try:
            new_url = url.replace('www.reddit', 'old.reddit')
            resp = urllib.request.urlopen(new_url)
            soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
            for link in soup.find_all(class_='md'):
                self.comments.add(link.text)
        except:
            self.expiredlinks.add(url)
            
    
    def get_comments(self):
        return list(self.comments)
    
    def events(self,url, loop = 10):
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
                
    
# start = time.time()


# urlname = 'https://www.reddit.com/r/GrandTheftAutoV'
# obj = CommentsCrawler()
# obj.events(urlname)
# print("Time elapsed:")
# end = time.time()
# print(end - start)


# newurl = 'https://old.reddit.com/r/GrandTheftAutoV/comments/pcw5jf/hopefully_this_hasnt_been_done_before/'
# parser = 'html.parser'
# resp = urllib.request.urlopen(newurl)
# soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

# coms = set()
# for link in soup.find_all(class_='md'):
#     coms.add(link.text)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

