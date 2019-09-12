#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[2]:

print("Initial EDA")
print("*"*60)
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'data','raw','housing.csv'))
PACKAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'Common_Functions','read_data'))


# In[3]:


sys.path.insert(1, PACKAGE_PATH)


# In[4]:


from read_data_from_file import load_data


# In[5]:


import pandas as pd


# In[6]:


df=load_data(DATA_PATH)


# In[7]:

print("Have a look at data....")
# each row represents a block group: a block group typically has 600 to 30000 people,
#for simplicity lets call them district          
df.head()
print("-"*60)
print("Insights:")
print("each row represents a block group: a block group typically has 600 to 30000 people,\nfor simplicity lets call them district")  
print("-"*60,'\n')
# In[8]:

print("Look at the basic info about data...")
print(df.info())
print("Insights:")
print("There are total 20640 rows\nall columns are of *float64* data type except *ocean_proximity*\nThere are null values in *total_bedrooms* column")
print("-"*60)


# In[9]:

print("Number of unique values in each column:\n")
print(df.nunique())
print("Insights:")
print("*ocean_proximity* is categorical variable")
print("-"*60)


# In[10]:

print("Value counts of *ocean_proximity* column:\n")
print(df['ocean_proximity'].value_counts())
print("-"*60)


# In[11]:

print("Descriptive Statistics of data...:\n")
print(df.describe())
print("Insights:")
print("Above is the descriptive statistics of data ignoring null values")
print("-"*60)

print("Univariate anlysis: Histograms")
df.hist(bins=50,figsize=(20,15))
print("Insights:")
print("The median income attribute does not look like it is expressed in US dollars. Data is scaled and capped at 15 for higher median incomes, and at 0.5 for lower median incomes.\nthe housing median age and median house values are also capped.\nMany histograms are tail heavy.")
plt.show()
print("-"*60)
print("*"*60)
