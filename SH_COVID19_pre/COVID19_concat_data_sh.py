#!/usr/bin/env python
# coding: utf-8

# In[200]:


import pandas as pd


# # 파일 불러오기

# In[235]:


df = []


# In[22]:


df1 = pd.read_csv('./data_COVID/COVID19_Seoul.csv', index_col=0)

df2 = pd.read_csv('./data_COVID/COVID19_Busan.csv',engine = 'python', index_col=0)

df3 = pd.read_csv('./data_COVID/COVID19_Daegu.csv',engine = 'python', index_col=0)  

df4 = pd.read_csv('./data_COVID/COVID19_Incheon.csv',engine = 'python', index_col=0)

df5 = pd.read_csv('./data_COVID/COVID19_Gwangju.csv',engine = 'python', index_col=0)

df6 = pd.read_csv('./data_COVID/COVID19_Daejeon.csv',engine = 'python', index_col=0)

df7 = pd.read_csv('./data_COVID/COVID19_Ulsan.csv',engine = 'python', index_col=0)

df8 = pd.read_csv('./data_COVID/COVID19_Sejong.csv',encoding = 'utf-8', index_col=0)

df9 = pd.read_csv('./data_COVID/COVID19_Kyeonggi.csv',engine = 'python', index_col=0)

df10 = pd.read_csv('./data_COVID/COVID19_Gangwon.csv',engine = 'python', index_col=0)

df11 = pd.read_csv('./data_COVID/COVID19_Chungbuk.csv',engine = 'python', index_col=0)

df12 = pd.read_csv('./data_COVID/COVID19_Jeonbuk.csv', engine = 'python', index_col=0)

df13 = pd.read_csv('./data_COVID/COVID19_Sejong.csv',engine = 'python', index_col=0)

df14 = pd.read_csv('./data_COVID/COVID19_Jeonnam.csv',engine = 'python', index_col=0)

df15 = pd.read_csv('./data_COVID/COVID19_Kyungbook.csv',engine = 'python', index_col=0)

df16 = pd.read_csv('./data_COVID/COVID19_Kyeongnam.csv',engine = 'python', index_col=0)

df17 = pd.read_csv('./data_COVID/COVID19_Jeju.csv',engine = 'python', index_col=0)


# In[234]:


df4 = pd.read_csv('./data_COVID/COVID19_Incheon.csv', index_col=0)


# In[257]:


df[3]['지역'] = '인천'


# In[258]:


df[3]


# In[236]:


df.append(pd.read_csv('./data_COVID/COVID19_Seoul.csv', index_col=0))


# In[237]:


df.append(pd.read_csv('./data_COVID/COVID19_Busan.csv',engine = 'python', index_col=0))#,encoding = 'utf-8'


# In[238]:


df.append(pd.read_csv('./data_COVID/COVID19_Daegu.csv',engine = 'python', index_col=0) )


# In[239]:


df.append(pd.read_csv('./data_COVID/COVID19_Incheon.csv', index_col=0))


# In[240]:


df.append(pd.read_csv('./data_COVID/COVID19_Gwangju.csv',engine = 'python', index_col=0))


# In[241]:


df.append(pd.read_csv('./data_COVID/COVID19_Daejeon.csv',engine = 'python', index_col=0))


# In[242]:


df.append(pd.read_csv('./data_COVID/COVID19_Ulsan.csv',engine = 'python', index_col=0))


# In[243]:


df.append(pd.read_csv('./data_COVID/COVID19_Sejong.csv',encoding = 'utf-8', index_col=0))


# In[244]:


df.append(pd.read_csv('./data_COVID/COVID19_Kyeonggi_2.csv',engine = 'python', index_col=0))


# In[245]:


df.append(pd.read_csv('./data_COVID/COVID19_Gangwon.csv',engine = 'python', index_col=0))


# In[246]:


df.append(pd.read_csv('./data_COVID/COVID19_Chungbuk.csv', index_col=0))


# In[247]:


df.append(pd.read_csv('./data_COVID/COVID19_Chungnam.csv', index_col=0))


# In[248]:


df.append(pd.read_csv('./data_COVID/COVID19_Jeonbuk.csv',engine = 'python', index_col=0))


# In[249]:


df.append(pd.read_csv('./data_COVID/COVID19_Jeonnam.csv', index_col=0))


# In[250]:


df.append(pd.read_csv('./data_COVID/COVID19_Kyungbook.csv',engine = 'python', index_col=0))


# In[251]:


df.append(pd.read_csv('./data_COVID/COVID19_Kyeongnam.csv', index_col=0))


# In[252]:


df.append(pd.read_csv('./data_COVID/COVID19_Jeju.csv',engine = 'python', index_col=0))


# # 데이터 불러오기

# In[259]:


df[3]


# In[23]:


df1


# In[22]:


df2


# In[29]:


df3


# In[233]:


df4


# In[41]:


df5


# In[42]:


df6


# In[43]:


df7


# In[44]:


df8


# In[63]:


df9


# In[46]:


df10


# In[47]:


df11


# In[48]:


df12


# In[49]:


df13


# In[50]:


df14


# In[51]:


df15


# In[52]:


df16


# In[53]:


df17


# # 데이터 Concat

# In[53]:


df1
df2
df3
df4 

df5 
df6 
df7
df8
df9 
df10 

df11
df12
df13
df14
df15

df16
df17


# In[260]:


df_covid19 = pd.DataFrame()

for a in range(0,17):
    df_covid19 = pd.concat([df_covid19, df[a]])
print(df_covid19.info())


# In[261]:


df_covid19.to_csv('COVID19_data.csv')

