#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver


# In[4]:


options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


# In[ ]:


driver = webdriver.Chrome('chromedriver', options=options)


# In[5]:


patient_number = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[8]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]').text
date = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[8]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').text
home = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[8]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]').text
infection_case = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[8]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]').text


# In[188]:


print(patient_number)
print(date)
print(home)
print(infection_case)


# In[197]:


# 테이블 읽어오기
# table = [ df1, df2, df3]
# 테이블은 데이터 프레임을 갖고있는 리스트인 것, 데이터 프레임 하나만 불러오더라도 리스트임을 잊지말것
df = pd.read_html('https://www.seoul.go.kr/coronaV/coronaStatus.do')
print(df)


# In[214]:


df[3]


# In[213]:


df[3].to_csv('Seoul_COVID.csv')

