#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Name : ')
print('Plot a line graph to find the average cholestrol found in various age groups')
print('Plot a line graph to find the correlation between systolic and diastolic blood pressure found in various age groups')


# In[2]:


#Task 1 
#Import all the libraries and read cardiovascular.csv
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('cardiovascular.csv')
df.dtypes


# # Average cholestrol found in various age groups

# In[3]:


#Task 2 
#Group by age and find the average cholesterol and make a dataframe out of it

group_by_age = df.groupby('age')['cholesterol'].mean().reset_index()

group_by_age


# In[4]:


#Task 3 
#Plot a line graph for various age group and their cholesterol 

label = group_by_age['age']
value = group_by_age['cholesterol']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average cholesterol" , linewidth=3.0)

plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Average Cholesterol in various age groups', fontsize=20)

plt.legend()

plt.show()


# Conclusion - The above graph shows how cholesterol start increasing after the age of 30

# # Correlation between systolic and diastolic blood pressure

# In[5]:


# Diastolic blood pressure - is the pressure in the arteries when the heart rests between beats
# Systolic blood pressure - the pressure in your arteries when your heart beats

#predefine code for image
from IPython.display import Image
Image(filename='blood pressure readings chart.jpg') 
#predefine code end


# In[6]:


#Task 4
#Group by age and find maximum systolic blood pressure and create a dataframe project out of it
group_by_age_systolic = df.groupby('age')['systolic_blood_pressure'].max().reset_index()
group_by_age_systolic.dtypes


# In[7]:


#Task 5
#Group by age and find maximum diastolic blood pressure and create a dataframe project out of it

group_by_age_diastolic = df.groupby('age')['diastolic_blood_pressure'].max().reset_index()

group_by_age_diastolic


# In[8]:


#Task 6
#Plot a line graph to show a Correlation between systolic and diastolic blood pressure
group_by_age_systolic_label = group_by_age_systolic['age']
group_by_age_systolic_value = group_by_age_systolic['systolic_blood_pressure']


fig1 = plt.subplots(figsize=(19,8))

plt.plot(group_by_age_systolic_label, group_by_age_systolic_value, label = "Average Systolic Blood Pressure" , linewidth=3.0)


group_by_age_diastolic_label = group_by_age_diastolic['age']
group_by_age_diastolic_value = group_by_age_diastolic['diastolic_blood_pressure']

plt.plot(group_by_age_diastolic_label, group_by_age_diastolic_value, label = "Average Diastolic Blood Pressure" , linewidth=3.0)
plt.xlabel('Age', fontsize =20)
plt.ylabel('Blood Pressure', fontsize =20)

plt.title('Corelation between systolic Blood Pressure and diastolic Blood Pressure blood pressure in various age groups', fontsize=20)

plt.legend()

plt.show()


# Conclusion - This says that the maximum systolic blood pressure is usually more than maximum diastolic blood pressure between 45 to 60

# In[ ]:





# In[ ]:




