#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd


# In[2]:


MODEL_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,'models'))


# In[3]:


print(os.listdir(MODEL_PATH))
dir_list = [i for i in os.listdir(MODEL_PATH) if i != '.gitkeep']
dir_list


# In[4]:


for dir_name in dir_list:
    print('\nDirectory name is ', dir_name)
    DIR_PATH = os.path.join(MODEL_PATH,dir_name)
    FILE_PATH = os.path.join(DIR_PATH, 'cross_val_scores.csv')
    print(pd.read_csv(FILE_PATH))


# **Insights**
# 1. After looking at cross validation scores, we can say that, Random forest is most stable base model.
