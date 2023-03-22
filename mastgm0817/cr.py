from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
# pip install webdriver_manager
import time
import pandas as pd

from bs4 import BeautifulSoup
import requests

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = "https://lol.ps/statistics"
driver.get(url)


champ_info = {}

time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="section_tierlist"]/div[2]/div[1]/div[6]').click()

for i in range(1,228):
  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[1]/span'
  name_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 이름 추가
  champ_info[i] = {}
  champ_info[i]["Name"] = name_text

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[1]/div[4]/span'
  position_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 포지션 추가
  champ_info[i]["Position"] = position_text

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[2]/div[1]'
  ps_score_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 PS Score 추가
  champ_info[i]["PS Score"] = ps_score_text

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[2]/div[3]'
  win_rate_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 Win Rate 추가
  champ_info[i]["Win Rate"] = win_rate_text
  

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[2]/div[4]'
  picked_rate_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 Pick Rate 추가
  champ_info[i]["Pick Rate"] = picked_rate_text

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[2]/div[5]'
  banned_rate_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 Ban Rate 추가
  champ_info[i]["Ban Rate"] = banned_rate_text

  xpath = '//*[@id="section_tierlist"]/div[3]/div[2]/a['+ str(i) +']/div[2]/div[6]'
  total_played_text = driver.find_element(By.XPATH, xpath).text

  # 딕셔너리에 total Played 추가
  champ_info[i]["total_played"] = total_played_text
  # # 스크롤 포인트 지정
  print(f'{i}번 완료')
  #   # ActionChains 객체 생성
  # actions = ActionChains(driver)

  # # 스크롤
  # actions.move_to_element(element).perform()

  # # 스크롤 2
  # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


df = pd.DataFrame(champ_info)
df = df.transpose()
df.to_csv('C:\\Users\\HomePC2\\Crawling\\lol.csv', index=True)

driver.quit()
