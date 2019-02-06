#serp.py
#authored by jgam


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import csv
import os
import xlwt
from datetime import date

today = str(date.today())

#input : keyywords
#output: ranks-websites-contents
def serp(keywords):
	#keywords = 'ascent'
	driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
	index = 0
	rank = 0
	#ret_dict includes keys as ranks and values as list of elements in this order: title, url, and contents
	ret_dict = dict()
	for keyword in keywords:
		driver.get('https://www.yahoo.co.jp')
		search = driver.find_element_by_name('p')
		search.send_keys(keyword)
		search_button = driver.find_elements_by_xpath("//*[@id=\"srchbtn\"]")[0]
		search_button.click()
		time.sleep(1)

		#now get the top 10 serps websites
		rank_info = []

		for i in range(10):
			rank_info = []
			index += 1
			try:
				urls = driver.find_element(By.XPATH, "//*[@id=\"WS2m\"]/div["+str(index)+"]/div[2]/div/span[1]")
			except:
				index += 1
				print('except index is ; ', index)
				urls = driver.find_element(By.XPATH, "//*[@id=\"WS2m\"]/div["+str(index)+"]/div[2]/div/span[1]")
			titles = driver.find_element(By.XPATH, "//*[@id=\"WS2m\"]/div["+str(index)+"]/div[1]/h3/a")#.get_attribute('innerHTML')
			print(titles.text)
			print('index is ; ', index)
			print(urls.text)
			
			#contents
			if 'youtube' in urls.text:
				contents = driver.find_element(By.XPATH, "//*[@id=\"WS2m\"]/div["+str(index)+"]/div[2]/div[2]/div[2]/p[1]")
			else:
				contents = driver.find_element(By.XPATH, "//*[@id=\"WS2m\"]/div["+str(index)+"]/div[2]/p")
			#//*[@id="WS2m"]/div[11]/div[2]/div[2]/div[2]/p[1]
			#//*[@id="WS2m"]/div[10]/div[2]/p

			print(contents.text)

			rank_info.append(titles.text)
			rank_info.append(urls.text)
			rank_info.append(contents.text)


			#finally add info to dict
			rank+=1
			ret_dict[rank] = rank_info


	print('the length of dictionary is ; ',len(ret_dict))
	return ret_dict

#create dictionary(hardcoding) for language and region
human_language = {'Korean':'kr', 'Japanese':'ja', 'English':'en'}
geo_location = {'Korea':'ka', 'Japan':'jp', 'global':'en'}

#language = input('type language: ')
#location = input('type location: ')
#keyword = input('type keyword separated by comma, if you have more than 5 keywords, input 0 : ').split(',')

keyword = ['ascent']
data = serp(keyword)
output = csv.writer(open("output.csv", 'w'))
for key,val in data.items():
	output.writerow([key, val])

print(data)