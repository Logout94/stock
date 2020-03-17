#!/usr/bin/env python3

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

main_rate=[]
main_index=[]
result={}

HOME="https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=ghks&o=1&q=%ED%99%98%EC%9C%A8"

def get_data():
	get_page = requests.get(HOME)
	exchange_rate = get_page.text
	soup = BeautifulSoup(exchange_rate, 'html.parser')

	return soup

def main():
	soup = get_data()
	ex_rate = soup.select('.wrap_rate tr td span')
	ex_index = soup.select('.wrap_rate tr td a')
	
	for ex in ex_rate:
		main_rate.append(ex.text)

	r = np.array(main_rate).reshape(-1,4)
	
	for rate, index in zip(r, ex_index):
		tmp = rate[0].split(',')
		result[index.text.split(' ')[1]] = float(''.join(tmp))
	
	print(result)




if __name__=="__main__":
	main()
