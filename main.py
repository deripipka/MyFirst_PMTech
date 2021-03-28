from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from bs4 import BeautifulSoup


def inp_inn():
    ogrn_inn = input('Введите ИНН или ОГРН для поиска: ')
    if ogrn_inn.isdigit() and (len(ogrn_inn) == 10 or len(ogrn_inn) == 13):
        return ogrn_inn
    else:
        print('Введено неправильное значение, попробуйте еще раз: ')
        inp_inn()


def scrap(param):
    driver = webdriver.Firefox(executable_path=r'C:\Users\derip\PycharmProjects\geckodriver.exe')
    driver.get("https://www.list-org.com/")
    assert "List-Org" in driver.title
    elem1 = driver.find_element_by_xpath("//input[@class='search_input']")
    elem1.send_keys(param, Keys.ENTER)
    sleep(randint(2, 4))
    elem2 = driver.find_element_by_class_name('org_list')
    driver.find_element_by_tag_name('label').find_element_by_tag_name('a').click()
    driver.get(driver.current_url)
    html = driver.page_source
    driver.close()
    return html


def parser(html):
    bs = BeautifulSoup(html, 'lxml')
    return bs


parser(scrap(inp_inn()))




#
#
#
#
# print(elem2.text)
# print(bs.find('div', class_='content').get_text())
# print(bs.find('td', class_='wwbw').get_text())
