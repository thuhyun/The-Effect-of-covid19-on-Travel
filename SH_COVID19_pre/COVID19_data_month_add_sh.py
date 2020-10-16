#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[27]:


df2 = pd.read_csv('COVID19_Jeonbuk.csv', index_col=0)


# In[24]:


df2 = pd.read_csv('re_COVID19_Kangwon.csv.csv', index_col=0)


# In[39]:


df3 = pd.read_csv('al_COVID19_Gwangju.csv', index_col=0)


# In[40]:


df4 = pd.read_csv('al_COVID19_kangwon.csv', index_col=0)


# In[41]:


df5 = pd.read_csv('al_COVID19_Jeonbuk.csv', index_col=0)


# # 데이터 info

# In[80]:


df1


# In[25]:


df2


# In[14]:


df3


# In[15]:


df4


# In[16]:


df5


# # 월 일 변경

# In[5]:


df2['확진일자'] = df2['확진일자'].astype(str).str.replace('월', '.')


# In[22]:


df2['확진일자'] = df2['확진일자'].astype(str).str.replace('일', '')


# In[31]:


df2['확진일자'] = df2['확진일자'].astype(str)


# In[34]:


df2


# In[33]:


for i in range(0,len(df2)):
     df2['확진일자'][i] = '2020.' + df2['확진일자'][i]


# In[23]:


test_df = pd.DataFrame(a_list)
test_df.head()


# In[7]:


a = df2['확진일자']


# In[9]:


type(a)


# In[15]:


a = a.astype(str)


# In[16]:


a


# In[8]:


df2.to_csv('COVID19_Jeonbuk.csv')


# In[17]:


b = []

for i in range(len(a)):
    b.append('2020' + a[i])
b = df2['확진일자']


# In[18]:


b


# In[29]:


# 2020 붙이는 코드 


df2=[]

for i in range(len(df2['확진일자'])):
    df2.append('2020.' + df2['확진일자'][i])
df2['확진일자']=df2


# # 확진월 만들기

# In[44]:


df2


# In[43]:


# 확진월 컬럼 추가
df2['확진월'] = ''


# In[38]:


df2['확진일자'][0].split('.')[0] + '-' + df2['확진일자'][0].split('.')[1]


# In[47]:


df2['확진일자'] = pd.to_datetime(df2['확진일자'])


# In[48]:


a_list = []
for a in range(len(df2['확진일자'])):
    a_list.append(str(df2['확진일자'][a]))


# In[49]:


df2['확진일자'] = a_list


# In[50]:


# 확진일자 00:00:00 제거하기
for i in range(0, len(df2)):
    df2['확진일자'][i] = df2['확진일자'][i].split(' ')[0] 


# In[51]:


df2


# In[52]:


# 확진월 컬럼 추가
df2['확진월'] = ''

df2['확진일자'][0].split('-')[0] + '-' + df2['확진일자'][0].split('-')[1]

# 확진일자를 -로 split하고 앞에 두개 따오기
for i in range(0, len(df2)):
    df2['확진월'][i] = df2['확진일자'][i].split('-')[0] + '-' + df2['확진일자'][i].split('-')[1]


# In[53]:


df2


# In[54]:


df2.to_csv('./datetime_month_Jeonbuk_COVID.csv')


# # 9월, 10월 제거

# In[55]:


import pandas as pd

# 충남
df = pd.read_csv('./datetime_month_Jeonbuk_COVID.csv', index_col= 0)
df.head()

# 10월 제거
a_list = []
for i in range(0, len(df)):
    if df['확진월'][i].split('-')[1] != '10':
        data = df.iloc[i]
        a_list.append(data)

df2 = pd.DataFrame(a_list)
df2.reset_index(drop=True, inplace= True)

df2.head()

# 9월 제거
a_list = []
for i in range(0, len(df2)):
    if df2['확진월'][i].split('-')[1] != '09':
        data = df2.iloc[i]
        a_list.append(data)

df3 = pd.DataFrame(a_list)
df3.reset_index(drop=True, inplace= True)

df3.head()

df3.to_csv('./datetime_month_Jeonbuk_COVID.csv')


# In[56]:


pd.read_csv('./datetime_month_Jeonbuk_COVID.csv')


# In[ ]:




