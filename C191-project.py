#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("This is a CSV of more than 200 rows which has Covide data.")
print("The task is to find out top 5 the countries who are least affected by covid")
print("Another task is to find out top 5 the countries who has the maximum number of deaths")
print("Another task is to find out top 5 the countries who has the maximum number of active cases")


# In[2]:


#Covide Data 
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataframe = pd.read_csv('covid19.csv')
df = dataframe.dropna()
df


# In[3]:


#Task 1 
#Sort the data as per total number of cases
sorted_df = df.sort_values(by=['total_cases'])
sorted_df


# In[4]:


#Task 2
#Get top 5 countries who has the least number of cases and plot a bar graph

least_cases = sorted_df['total_cases'].head(5)
least_cases_country = sorted_df['country'].head(5)

print(least_cases)
print(least_cases_country)

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("Covid Cases")


label = least_cases_country
value = least_cases 
plt.bar(label, value,width=0.4, color=('purple','yellow','green','blue' , 'red')) #bar-grap


# In[5]:


#Task 3
#Sort the data as per total number of deaths

sorted_df = df.sort_values(by=['total_deaths'])
sorted_df


# In[6]:


#Task 4
#Get top 5 countries who has the maximum number of deaths and plot a bar graph

highest_deaths = sorted_df['total_deaths'].tail(5)
highest_deaths_country = sorted_df['country'].tail(5)

print(highest_deaths)
print(highest_deaths_country)

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("Covid Cases")


label = highest_deaths_country
value = highest_deaths 
plt.bar(label, value,width=0.4, color=('purple','yellow','green','blue' , 'red')) #bar-grap


# In[7]:


#Task 5
#Sort the data as per active cases

sorted_df = df.sort_values(by=['active_cases'])
sorted_df


# In[8]:


#Task 6
#Get top 5 countries who has the maximum number of active cases and plot a bar graph

active_cases = sorted_df['active_cases'].tail(5)
active_cases_country = sorted_df['country'].tail(5)

print(active_cases)
print(active_cases_country)

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("Covid Cases")


label = active_cases_country
value = active_cases 
plt.bar(label, value,width=0.4, color=('purple','yellow','green','blue' , 'red')) #bar-grap


# In[ ]:





# In[ ]:




