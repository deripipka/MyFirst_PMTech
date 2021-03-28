from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from bs4 import BeautifulSoup

ogrn_inn = input('Введите ИНН или ОГРН для поиска: ')
driver = webdriver.Firefox(executable_path=r'C:\Users\derip\PycharmProjects\geckodriver.exe')
driver.get("https://www.list-org.com/")

assert "List-Org" in driver.title
elem1 = driver.find_element_by_xpath("//input[@class='search_input']")
elem1.send_keys(ogrn_inn, Keys.ENTER)
sleep(randint(1, 3))
elem2 = driver.find_element_by_class_name('org_list')
driver.find_element_by_tag_name('label').find_element_by_tag_name('a').click()
driver.get(driver.current_url)
html = driver.page_source
driver.close()

bs = BeautifulSoup(html, 'lxml')

print(elem2.text)
# print(bs.find('div', class_='content').get_text())
# print(bs.find('td', class_='wwbw').get_text())
