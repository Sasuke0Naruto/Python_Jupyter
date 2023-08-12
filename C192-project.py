#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("This is a CSV of more than 1300 rows which has bmi data.")
print("The task is to find out what is the percentage of people who are underweight and healthy. And plot a pie chart around it")
print("Another task is to find out what is the percentage of male and female who are underweight and healthy. And plot a pie chart around it")


# In[2]:


#BMI Data

#predefine code
import pandas as pd
import matplotlib .pyplot as plt

dataframe = pd.read_csv("bmi.csv")
df = dataframe.dropna()
bmi = df['bmi']
df


# In[3]:


#Task 1
#How many people are underweight and create a dataframe out of it

underweight_dataframe = df.loc[bmi < 18.5]['gender'].reset_index(name='gender')
print(underweight_dataframe)

underweight_count = underweight_dataframe['index'].count()
print(underweight_count)


# In[4]:


#Task 2
#How many people have normal weight and create a dataframe out of it

healthy_weight_dataframe = df.loc[(bmi > 18.5) & (bmi < 24.9)]['gender'].reset_index(name='gender')
print(healthy_weight_dataframe)

healthy_weight_count = healthy_weight_dataframe['index'].count()
print(healthy_weight_count)


# In[5]:


#Task 3
#Plot a pie chart as per the percentage of male and female who are underweight, and healthy. 

value = [underweight_count,healthy_weight_count]
label = ["underweight","healthy_weight"]
plt.pie(value,labels=label, autopct='%0.2f%%', radius=2)
plt.show()


# In[6]:


#Task 4
#Group by the gender from underweight dataframe
group_underweight = underweight_dataframe.groupby('gender')['gender'].count().reset_index(name='number')
group_underweight


# In[7]:


#Task 5
#Plot a pie chart as per the percentage of male and female who are underweight
value = group_underweight['number']
label = group_underweight['gender']
plt.pie(value,labels=label, autopct='%0.2f%%', radius=2)
plt.show()


# In[8]:


#Task 6
#Group by the gender from healthy weight dataframe

group_healthy_weight = healthy_weight_dataframe.groupby('gender')['gender'].count().reset_index(name='number')
group_healthy_weight


# In[9]:


#Task 7
#Plot a pie chart as per the percentage of male and female who are healthy
value = group_healthy_weight['number']
label = group_healthy_weight['gender']
plt.pie(value,labels=label, autopct='%0.2f%%', radius=2)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




