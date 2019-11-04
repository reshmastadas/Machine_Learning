#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[2]:

print("EDA of train_df")
print("*"*60)
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'data','interim','train_df.csv'))
PACKAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'Common_Functions','read_data'))


# In[3]:


sys.path.insert(1, PACKAGE_PATH)


# In[4]:


train_df = pd.read_csv(DATA_PATH)


# In[5]:


housing = train_df.copy()


# In[6]:

print("\nScatter plot: For High level visualization")
housing.plot(kind = 'scatter', x='longitude', y='latitude')
plt.show()
print("Insights:")
print("Data points look like california. But it is hard to see any  pattern. Lets set alpha to 0.1")

print("-"*60)
# In[7]:


housing = train_df.copy()


# In[8]:

print("Scatter plot: for data density visualization")
housing.plot(kind = 'scatter', x='longitude', y='latitude', alpha=0.1)
plt.show()
print("Insights:")
print("We can clearly see high-density areas like the Bay Area and around Los Angeles and San Diego\n plus long line of fairly high density in the Central Valley in particular around Sacramento and Fresno")

# In[9]:

print("-"*60)

print("Scatter plot: for detailed data visualization")
# set population as circle diameter, set color as median house value
housing.plot(kind = 'scatter', x='longitude', y='latitude', alpha=0.4, s = housing['population']/100, label = 'poplulation'
            ,figsize=(10,7),c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True)
plt.show()
print("Insights:")
print("Housing prices are very much realated to the location and to the population density.")

# In[10]:

print("-"*60)


corr_matrix = housing.corr()


# In[11]:


print("Correlation of columns with target")
print(corr_matrix['median_house_value'].sort_values(ascending=False))


print("Insights:")
print("population, population_per_household, longitude, latitude, bedrooms_per_room has some slight negative correlation.")

print("-"*60)
# In[12]:
print("scatter matrix of data: To analyze correlation in depth")
from pandas.plotting import scatter_matrix
attributes = ['median_house_value','median_income','total_rooms','housing_median_age','latitude']
scatter_matrix(housing[attributes],figsize=(12,8))
plt.show()


# **Insights**
# 1. correlation of median_house_value to median_income is strong.

# In[13]:


print("-"*60)
print("Scatter plot between median_house_value and median_income")
housing.plot(kind = 'scatter', y='median_house_value',x='median_income')
plt.show()
print("Insights:")
print("horizontal line at 500000 is obvious due to the cap value.")
print("horizontal lines at 450000, 350000, 280000 are some data querks which can be removed by removing some data points.")

print("-"*60)
print("*"*60)