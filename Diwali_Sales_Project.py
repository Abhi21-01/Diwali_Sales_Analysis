#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv(r"C:\Users\singa\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv", encoding = "ISO-8859-1")


# In[6]:


df


# In[7]:


df.drop(columns = ['Status', 'unnamed1'], inplace = True)


# In[8]:


df


# In[9]:


df.shape


# In[10]:


df.head(100)


# In[19]:


df.info()


# In[20]:


pd.isnull(df)


# In[21]:


pd.isnull(df).sum()


# In[22]:


df.dropna(inplace = True)


# In[23]:


df.shape


# In[24]:


df['Amount'] = df['Amount'].astype('int')


# In[25]:


df.dtypes


# In[55]:


df[['Age', 'Orders', 'Amount']].describe()


# # Final Table

# In[56]:


df


# # Exploratory Data Analysis

# ## Correlation Analysis

# In[97]:


df.corr(numeric_only = True)


# In[98]:


sns.heatmap(df.corr(numeric_only = True), annot = True)


# ##### This is clearly showing no correlation between the numeric values of different columns. 

# ## Gender

# In[28]:


df.columns


# In[29]:


ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[100]:


sns.barplot(x = 'Gender', y= 'Amount', data = sales_gen)


# ##### From above graphs it is clear that most of the buyers are females and even the purchasing power of females are greater than men.

# ## Age

# In[46]:


ax = sns.countplot(x = 'Age Group', data = df, hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_age_grp = df.groupby(['Age Group'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[99]:


sns.barplot(x = 'Age Group', y= 'Amount', data = sales_age_grp)


# ##### From above graphs we can see that most of the buyers are of age group 26-35 years female 

# ## State 

# In[49]:


sales_state_orders = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False)


# In[52]:


sns.set(rc={'figure.figsize': (20,5)})
sns.barplot(x = 'State', y= 'Orders', data = sales_state_orders )


# In[54]:


sales_state_amount = df.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)
sns.barplot(x = 'State', y= 'Amount', data = sales_state_amount )


# ##### From the above analysis using graphs, it is clear that most of orders & total sales are from Uttar Pradesh, Maharashtra and Karnataka. 

# ## 	Marital Status 

# In[65]:


ax = sns.countplot(x = 'Marital_Status', data = df)
sns.set(rc={'figure.figsize': (6,10)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[70]:


sales_marital_amount = df.groupby(['Marital_Status', 'Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[73]:


sns.set(rc={'figure.figsize': (6,2)})
sns.barplot(x = 'Marital_Status', y= 'Amount', data = sales_marital_amount, hue = 'Gender' )


# ##### From above graph it is clear that most of the buyers are married woman. 

# ## Occupation 

# In[76]:


sns.set(rc={'figure.figsize': (15,2)})
sns.countplot(x = 'Occupation', data = df)


# In[78]:


sales_occupation_amount = df.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[79]:


sns.barplot(x = 'Occupation', y= 'Amount', data = sales_occupation_amount)


# ##### Most of the buyers are working in the IT Sector, Healthcare and Aviation. 

# ## Product Category 

# In[82]:


sns.set(rc = {'figure.figsize' : (20, 5)})
sns.countplot(x='Product_Category', data =  df)


# In[88]:


sales_product_amount = df.groupby(['Product_Category'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)


# In[89]:


sns.barplot(x = 'Product_Category', y= 'Amount', data = sales_product_amount)


# In[93]:


sales_product_ID_orders = df.groupby(['Product_ID'], as_index= False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)


# In[94]:


sns.barplot(x = 'Product_ID', y= 'Orders', data = sales_product_ID_orders)


# # Conclusion

# ##### Married women of age group 26-35 years from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely to purchase products from Food, Apparel and Electronics category.
