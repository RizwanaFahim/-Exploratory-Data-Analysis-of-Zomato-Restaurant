#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Set Analysis & Visualization

# Importing Libraries
# 

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')


# Reading CSV

# In[18]:


df=pd.read_csv(r"D:/Downloads/zomato/zomato.csv")
df.head()


# In[19]:


df.shape


# In[20]:


df.columns


# In[21]:


df=df.drop(['url', 'address', 'dish_liked','phone','menu_item','reviews_list'],axis=1)


# In[22]:


df.head()


# In[23]:


df.info()


# In[24]:


df.drop_duplicates(inplace=True)
df.shape


# Cleaning Rate Column

# In[25]:


df['rate'].unique()


# Removing "NEW" , "-" and "/5" from Rate Column

# In[26]:


def handlerate(value):
    if( value=='NEW' or value=='-'):
        return np.nan
    else:
        value=str(value).split('/')
        value=value[0]
        return float(value)
df['rate']=df['rate'].apply(handlerate)
df['rate'].head()


# In[27]:


df.isnull().sum()


# In[28]:


df.describe()


# Filling Null Values in Rate Column with Mean

# In[29]:


df['rate'].fillna(df['rate'].mean(),inplace=True)
df['rate'].isnull().sum()


# Dropping Null Values

# In[30]:


df.dropna(inplace=True)
df.head()


# In[31]:


df.rename(columns={'listed_in(type)':'Type','approx_cost(for two people)':'Cost2plates'},inplace=True)
df.head()


# In[32]:


df['location'].unique()


# In[33]:


df['listed_in(city)'].unique()


# Listed in(city) and location, both are there, lets keep only one.

# In[34]:


df.drop(['listed_in(city)'],axis=1,inplace=True)


# In[35]:


df.head()


# In[36]:


df['Cost2plates'].unique()


# Removing , from Cost2Plates Column

# In[37]:


def handlecomma(value):
    value=str(value)
    if ',' in value:
        value=value.replace(',','')
        return float(value)
    else:
        return float(value)
    
df['Cost2plates']=df['Cost2plates'].apply(handlecomma)



# In[38]:


df['Cost2plates'].unique()


# Cleaning Rest Type Column

# In[39]:


count=df['rest_type'].value_counts()


# In[40]:


rest_lessthan_1000=count[count<1000]
rest_lessthan_1000


# Making Rest Types less than 1000 in frequency as others

# In[41]:


def handleresttype(value):
    if (value in rest_lessthan_1000):
        return 'others'
    else:
        return value
df['rest_type']=df['rest_type'].apply(handleresttype)


# In[42]:


df['rest_type'].value_counts()


# In[43]:


df.head()


# Cleaning Cuisines Column

# In[44]:


count=df['cuisines'].value_counts()


# In[45]:


cuisines_lessthan_100=count[count<100]


# In[46]:


def handlecuisines(value):
    if(value in cuisines_lessthan_100):
        return 'others'
    else:
        return value
df['cuisines']=df['cuisines'].apply(handlecuisines)
df['cuisines'].value_counts()


# Cleaning Location Column

# In[47]:


df['location'].value_counts()


# In[48]:


location=df['location'].value_counts(ascending=False)


# In[49]:


location_lessthan_300=location[location<300]


# In[50]:


def handle_location(value):
    if(value in location_lessthan_300):
        return 'others'
    else:
        return value
    
df['location']=df['location'].apply(handle_location)

df['location'].value_counts()


# In[51]:


df['Type'].value_counts()


# Data is Clean, Lets jump to Visualization
# 

# Count Plot of Various Locations

# In[52]:


plt.figure(figsize=(16,10))
ax=sns.countplot(x="location", data=df)
plt.xticks(rotation=90)
plt.show()


# Visualizing Online Order

# In[53]:


plt.figure(figsize = (6,6))
sns.countplot(x='online_order',data=df, palette = 'inferno')


# In[54]:


df['Type'].value_counts()


# Visualizing Book Table

# In[55]:


plt.figure(figsize=(6,6))
ax=sns.countplot(x='book_table',data=df,palette='rainbow')
plt.show()


# Visualizing Online Order vs Rate

# In[56]:


sns.boxplot(x='online_order',y='rate',data=df)
plt.show()


# Visualizing Book Table vs Rate

# In[57]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'book_table', y = 'rate', data = df)


# Visualizing Online Order Facility, Location Wise

# In[58]:


df1=df.groupby(['location','online_order'])['name'].count()
df1.to_csv('location_online.csv')
df1=pd.read_csv('location_online.csv')
df1=pd.pivot_table(df1, values=None,index=['location'],columns=['online_order'],fill_value=0,aggfunc=np.sum)
df1


# In[59]:


df2=df.groupby(['location','book_table'])['name'].count()
df2.to_csv('location_booktable.csv')
df2=pd.read_csv('location_booktable.csv')
df2=pd.pivot_table(df2,values=None,index=['location'],columns=['book_table'],fill_value=0,aggfunc=np.sum)
df2


# In[60]:


df2.plot(kind='bar',figsize=(15,8))


# Visualizing Types of Restaurents vs Rate

# In[61]:


plt.figure(figsize=(14,8))
sns.boxplot(x='Type',y='rate',data=df,palette='inferno')


# Grouping Types of Restaurents, location wise

# In[62]:


df3=df.groupby(['location','Type'])['name'].count()
df3.to_csv('location_Type')
df3=pd.read_csv('location_Type')
df3=pd.pivot_table(df3,values=None,index=['location'],columns=['Type'],fill_value=0,aggfunc=np.sum)
df3


# No. of Votes, Location Wise

# In[63]:


df4=df[['location','votes']]
df4=df4.drop_duplicates()
df5=df4.groupby(['location'])['votes'].sum()
df5=df5.to_frame()
df5=df5.sort_values('votes',ascending=False)
df5.head()


# In[64]:


plt.figure(figsize=(15,8))
sns.barplot(x=df5.index,y=df5['votes'])
plt.xticks(rotation=90)


# Visualizing Top Cuisines

# In[65]:


df6=df[['cuisines','votes']]
df6=df6.drop_duplicates()
df7=df6.groupby('cuisines')['votes'].sum()
df7=df7.to_frame()
df7=df7.sort_values('votes',ascending=False)
df7.head()


# In[66]:


df7=df7.iloc[1:,:]
df7.head()


# In[67]:


plt.figure(figsize=(15,8))
sns.barplot(x=df7.index,y=df7['votes'])
plt.xticks(rotation=90)

