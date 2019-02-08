#serp.py
#authored by jgam

"""
possible db variables!
"""
#https://www.google.com/search?hl=ja&gl=jp&source=hp&ei=ejRZXLjNB8aD8wWM1ZWIAg&q=asdf&btnK=Google+%E6%A4%9C%E7%B4%A2&oq=asdf&gs_l=psy-ab.3..0i131j0j0i4j0l4j0i4.1642.1865..1995...0.0..0.102.463.6j1....2..0....1..gws-wiz.....0..0i131i4.tdRCy17kWQQ

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
def serp(keywords, region, language):
	#keywords = 'ascent'
	driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
	
	#ret_dict includes keys as ranks and values as list of elements in this order: title, url, and contents
	ret_list = []
	for keyword in keywords:
		ret_dict = dict()
		index = 0
		rank = 0
		first_index = 2
		driver.get('https://www.google.com/webhp?hl='+language+'&gl='+region+'&q='+keyword+'&num=20')#/search?hl=ko&gl=kr')
		search_button = driver.find_elements_by_xpath("//*[@id=\"tsf\"]/div[2]/div/div[3]/center/input[1]")[0]
		search_button.click()
		time.sleep(1)

		#now get the top 10 serps websites
		rank_info = []
		
		for i in range(10):
			rank_info = []
			print('the th interation: ', i)
			print(first_index, index)
			index += 1
			#제목
			try:
				titles = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(first_index)+"]/div/div["+str(index)+"]/div/div/div[1]/a/h3")
				print(titles.text)
			except:
				#not 1 but 2 because we skippping the pictures
				first_index += 2
				index = 1
				titles = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(first_index)+"]/div/div["+str(index)+"]/div/div/div[1]/a/h3")
				print(titles.text)
			
			#getting the urls, the second div is what we need to be numbering
			urls = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(first_index)+"]/div/div["+str(index)+"]/div/div/div[1]/a/div/cite")#.get_attribute('innerHTML')
			#//*[@id="rso"]/div[2]/div/div[2]/div/div/div[1]/a[1]/div/cite
			print(urls.text)
			
			#contents
			contents = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div["+str(first_index)+"]/div/div["+str(index)+"]/div/div/div[2]/div/span")
			print(contents.text)

			rank_info.append(contents.text)
			rank_info.append(titles.text)
			rank_info.append(urls.text)

			#finally add info to dict
			rank += 1
			ret_dict[rank] = rank_info
		ret_dict[0]=keyword
		ret_list.append(ret_dict)

	return ret_list

#create dictionary(hardcoding) for language and region
human_language = {'1':'kr', '3':'ja', '2':'en'}
geo_location = {'1':'ka', '3':'jp', '2':'en'}

###integer -> region, language
print('1. Korea(korean), 2. English(global), 3. Japan(japanese)')
language = input('type language: ')
location = input('type location: ')
keyword = input('type keyword separated by comma, if you have more than 5 keywords, input 0 : ').split(',')

file = 'input.csv'
keyword = []
with open(file) as f:
	reader = csv.reader(f)
	for i in reader:
		keyword.append(i[0])
print(keyword)
keyword = ['ascent','viva']
data = serp(keyword, geo_location[location], human_language[language])
print(data)
output = csv.writer(open("output.csv", 'w'))
output.writerow(['keyword','rank', 'title', 'contents', 'urls'])
for datum in data:
	output.writerow([datum[0]])
	del datum[0]
	for key,val in datum.items():
		output.writerow(['',key, val[0], val[1], val[2]])
print(data)
