#serp2.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import csv
import os
import xlwt
from datetime import date

from bs4 import BeautifulSoup

def get_serp(keywords, language, region):
	ret_list = []
	driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
	#for loop should be here with keywords
	keyword = 'galaxy s8 widget'
	for keyword in keywords:
		driver.get('https://www.google.com/webhp?hl='+language+'&gl='+region+'&q='+keyword+'&num=20')#/search?hl=ko&gl=kr')
		search_button = driver.find_elements_by_xpath("//*[@id=\"tsf\"]/div[2]/div/div[3]/center/input[1]")[0]
		search_button.click()
		time.sleep(1)
		titles = driver.find_elements_by_class_name("LC20lb")
		urls = driver.find_elements_by_class_name("iUh30")
		contents = driver.find_elements_by_class_name("st")
		ret_dict = {}
		ret_dict[0] = keyword
		for i in range(10):
			ret_dict[i+1]=[titles[i].text, urls[i].text, contents[i].text]
		ret_list.append(ret_dict)
	return ret_list

keywords = ['galaxy s8 widget', 'galaxy s6', 'iphone xr']
data = get_serp(keywords, 'ja', 'jp')
output = csv.writer(open("output.csv", 'w'))
output.writerow(['keyword','rank', 'title', 'urls', 'contents'])
for datum in data:
	output.writerow([datum[0]])
	del datum[0]
	for key,val in datum.items():
		output.writerow(['',key, val[0], val[1], val[2]])


#needs research
#actual_urls = driver.find_elements_by_xpath("//a[@href]")
#actual_urls = driver.find_elements_by_class_name("r")

#//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]
#//*[@id="rso"]/div[1]/div/div[2]/div/div/div[1]/a

#for i in range(10):
#	print(urls[i].text)
#	print(actual_urls[i].get_attribute("href"))

'''
for i in driver.find_elements_by_class_name("LC20lb"):
	print(i.text)

for i in driver.find_elements_by_class_name("iUH30"):
	print(i.text)

for i in driver.find_elements_by_class_name("st"):
	print(i.text)
'''
#print(driver.get_attribute('innerHTML'))
#class = "LC20lb"
#soup = BeautifulSoup(driver.get_attribute('innerHTML'),'html.parser')
#div_block = soup.find_all('div', attrs={'class':'g'})

#for result in div_block:
#	print(result)