#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


df = pd.read_csv(r"C:\Users\Sarthak Sarkar\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_5871594.csv")


# In[34]:


df


# In[35]:


df.head()


# In[36]:


df.tail()


# In[38]:


df.shape


# In[39]:


df.columns


# In[40]:


df.dtypes


# In[41]:


df.info()


# In[42]:


df.describe()


# In[44]:


df.duplicated().sum()


# In[45]:


df.isna().sum().any()


# In[46]:


df = df.fillna(method = "ffill")
df.head()


# In[47]:


df.isna().sum().any()


# In[48]:


df['Country Name'].unique()


# In[49]:


df['Country Code'].unique()


# In[50]:


df['Indicator Name'].unique()


# In[51]:


df['Indicator Code'].unique()


# In[52]:


df.drop(['Indicator Name','Indicator Code','Country Code'],axis = 1, inplace = True)


# In[53]:


df.columns


# In[54]:


cols = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975',
        '1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991',
       '1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007',
       '2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']


# In[56]:


for i in cols:
    fig = plt.figure(figsize=(5,5))
    plt.hist(df[i],color='#B22222',bins=10)
    plt.xlabel(i)
    plt.show()


# In[57]:


years = df.columns[1:]

total_values = df[years].sum()

plt.figure(figsize=(30,30))
plt.barh(years, total_values,color='#191970')
plt.xlabel('Total Values')
plt.ylabel('Year', size=20)
plt.title('Total Values per Year', size=20)
plt.show()


# In[58]:


country_by_1960 = df.sort_values(by='1960').head(20)
country_by_1960


# In[59]:


country_by_1960_t = country_by_1960.set_index('Country Name').T
for country_name, data_values in country_by_1960_t.iterrows():
    fig = plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Countries')
    plt.ylabel('Data Values')
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()

