
import os
import json,re
import requests
from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType



pdf_site_url = "https://dejt.jt.jus.br/cadernos/dejt.html"

def db_connection():
	database = "legal_data_mining"
	user = "legal_data_mining"
	password = "$5r@pasnckjasCC*S"
	host = "localhost"
	port = "5432"
	connection = psycopg2.connect(user=user,
	  password=password,
	  host=host,
	  port=port,
	  database=database
  	)
	return connection


def get_chromedriver(headless=True):
	try:
		capa = DesiredCapabilities.CHROME
		capa["pageLoadStrategy"] = "none"
		options = Options()
		options.add_argument('start-maximized')
		options.add_experimental_option("useAutomationExtension", False)
		options.add_experimental_option("excludeSwitches",["enable-automation"])
		if headless:
			options.add_argument('--headless')
		driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options,desired_capabilities=capa)
		driver.maximize_window()
		return driver
	except Exception as error:
		log.error(error)
		raise error

def get_data_from_pdf():
	try:
		driver.get(pdf_site_url)
		sleep(7)
		date_of_register = driver.find_element_by_xpath('//*[@id="tituloPagina"]/div[2]')
		table_data = driver.find_element_by_xpath('//*[@id="feriadoSel"]/fieldset/table').find_elements_by_tag_name('a')
		pdf_list = []
		for a_tag in table_data:
			pdf_url = a_tag.get_attribute("href")
			if pdf_url.endswith('.pdf'):
				pdf_list.append(pdf_url)
		print(len(pdf_list))
		for pdf_url in pdf_list:
			driver.get(pdf_url)
			file_name = pdf_url.rsplit('/', 1)[-1]
			sleep(5)

		html = driver.page_source
		soup = BeautifulSoup(html,'html.parser')
		sleep(5)
		driver.quit()
	except Exception as error:
		driver.quit()
		raise error


if __name__== "__main__":
	driver=get_chromedriver(headless=False)
	get_data_from_pdf()
