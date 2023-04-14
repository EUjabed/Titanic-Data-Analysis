#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# ## Merging 12 months of sales data into a single CSV file

# In[2]:


# Set the path to the directory containing the CSV files

path = "D:\Skill Developing\Google data Analytics\Data\Data for Project\SalesAnalysis\Sales_Data"


# In[3]:


# Get a list of all the CSV files in the directory

csv_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]


# In[4]:


# Combine all the CSV files into a single DataFrame

df = pd.concat((pd.read_csv(f) for f in csv_files))


# In[5]:


# Write the combined DataFrame to a new CSV file

df.to_csv("merged.csv", index=False)


# In[6]:


df.head()


# In[7]:


df.isnull().sum()


# In[8]:


df.tail()


# ## Handling null values

# In[9]:


# Counting the number of null values in each row
null_count = df.isnull().sum(axis=1)

### Counting the number of rows with null values
rows_with_null = len(null_count[null_count > 0])

print("Number of rows with null values:", rows_with_null)


# ### Deleting null values

# In[16]:


df.dropna(axis=0, inplace=True)
df.head()


# ## Augment data with some additional columns

# ### Add a month column

# In[11]:


# Converting the date column to a pandas datetime object
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M', errors='coerce')

# Extracting the month name from the date column
df['Month'] = df['Order Date'].dt.strftime('%B')


df.head()


# In[12]:


print(df["Month"].dtype)


# In[13]:


# Define the month names in the desired order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Convert the 'Month' column to a categorical data type with the desired order
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)


# In[14]:


df.head()


# In[17]:


df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])


# ### Add sales column

# In[18]:


df['Sales'] = df["Quantity Ordered"] * df["Price Each"]
df.head()


# In[19]:


df.tail()


# In[ ]:


print(df.iloc[517])


# # Question 1: What was the best month for sales? How much was earned that month?

# In[ ]:





# In[20]:


df.groupby("Month").sum()


# In[ ]:


df.plot.bar(x='Month', y='Sales')
plt.show()


# In[ ]:




