#!/usr/bin/env python
# coding: utf-8

# In[9]:


# importing libraries
import numpy as np # Importing the numpy library for array operations and mathematical functions
import pandas as pd # Use for exploring the data 
import seaborn as sns # it has also plot
import matplotlib.pyplot as plt # for some extra plot functions
import plotly.express as px # this library can makes interactive plots


# In[5]:


pip install numpy


# In[58]:


pip install seaborn


# In[59]:


pip install matplotlib


# In[8]:


pip install plotly


# In[10]:


# reading the data set
shop = pd.read_csv('shopping_trends_updated.csv')


# In[11]:


# rows and columns of the data set
shop.shape


# In[12]:


# Lets convert into excel format because it has less rows
shop.to_excel('shopping_trends_updated.xlsx')


# In[13]:


# it shows the first five rows of the data set 
shop.head()


# In[14]:


# it shows the data types of the variables and help us to identify what type of variable is
shop.dtypes


# In[15]:


# it shows the names of the columns 
shop.columns


# In[16]:


# it tells us the data type and null values and so much information
shop.info()


# In[17]:


shop.shape


# In[18]:


shop.isnull().sum()
# it has no null values or missing values


# In[19]:


# it is the important columns having unique values
print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")


# In[20]:


'''1.What is the overall distribution of customer ages in the dataset?

2.How does the average purchase amount vary across different product categories?

3.Which gender has the highest number of purchases?

4.What are the most commonly purchased items in each category?

5.Are there any specific seasons or months where customer spending is significantly higher?

6.What is the average rating given by customers for each product category?

7.Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?

8.Which payment method is the most popular among customers?

9.Do customers who use promo codes tend to spend more than those who don't?

10.How does the frequency of purchases vary across different age groups?

11.Are there any correlations between the size of the product and the purchase amount?

12.Which shipping type is preferred by customers for different product categories?

13.How does the presence of a discount affect the purchase decision of customers?

14.Are there any specific colors that are more popular among customers?

15.What is the average number of previous purchases made by customers?

16.How does the purchase amount differ based on the review ratings given by customers?

17.Are there any noticeable differences in purchase behavior between different locations?

18.Is there a relationship between customer age and the category of products they purchase?

19.How does the average purchase amount differ between male and female customers?'''


# In[21]:


# 1.Count of the each age value
shop['Age'].value_counts()


# In[22]:


#. mean or average value of age 
shop['Age'].mean()


# In[23]:


# .unique function shows the unique values of any columns
shop['Gender'].unique()


# In[25]:


# .we are cutting the age into some category and storing in the different column
shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults'
                                                                                             , 'old'] )


# In[26]:


# we use plotly library to use plots
fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()


# In[27]:


# it shows the names of the columns
shop.columns


# In[28]:


# unique values of Category
shop['Category'].unique()


# In[29]:


# we are seeking amount based on Category
shop.groupby('Category')['Purchase Amount (USD)'].mean()


# In[30]:


# names of columns
shop.columns


# In[91]:


# this is the seaborn plot
sns.barplot(data=shop, x='Gender', y='Purchase Amount (USD)')


# In[35]:


shop.columns


# In[36]:


# we are seeking Item purchased based on Category
shop.groupby('Category')['Item Purchased'].value_counts()


# In[37]:


fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()


# In[38]:


shop.columns


# In[39]:


shop['Season'].unique()


# In[40]:


# filtering the data 
shop[shop['Season'] == 'Summer'].value_counts().sum()


# In[41]:


# filtering the data 
shop[shop['Season'] == 'Winter'].value_counts().sum()


# In[42]:


# filtering the data 
shop[shop['Season'] == 'Spring'].value_counts().sum()


# In[43]:


# filtering the data 
shop[shop['Season'] == 'Fall'].value_counts().sum()


# In[44]:


fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )

fig.show()


# In[45]:


shop.columns


# In[46]:


shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()


# In[47]:


fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()


# In[48]:


shop.columns


# In[49]:


shop['Subscription Status'].unique()


# In[90]:


sns.barplot(data=shop, x='Subscription Status', y='Purchase Amount (USD)')


# In[51]:


shop['Purchase Amount (USD)'].sum()


# In[52]:


shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()


# In[53]:


shop.columns


# In[54]:


shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)


# In[55]:


shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()


# In[56]:


fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()


# In[89]:


sns.barplot(data=shop, x='Payment Method', y='Purchase Amount (USD)')


# In[61]:


shop.columns


# In[62]:


shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()


# In[63]:


fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()


# In[64]:


fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()


# In[65]:


# we are cutting the age into some category and storing in the different column
# shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults'
#                                                                                              , 'old'] )

shop[['Age' , 'Age_category']]


# In[66]:


shop['Age_category'].unique()


# In[67]:


shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()


# In[68]:


px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')


# In[69]:


shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()


# In[70]:


fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()


# In[71]:


shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)


# In[72]:


shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2,
                                                       'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})


# In[73]:


shop['Category'].unique()


# In[74]:


shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})


# In[75]:


shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()


# In[76]:


px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')


# In[77]:


fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')

fig.show()


# In[78]:


px.histogram(shop , x = 'Color')


# In[79]:


shop['Color'].value_counts().nlargest(5)


# In[80]:


shop['Previous Purchases'].mean()


# In[81]:


shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)


# In[82]:


shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()


# In[83]:


fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()


# In[84]:


shop_group = shop.groupby('Category')['Age'].mean().reset_index()


# In[85]:


fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()


# In[86]:


shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()


# In[87]:


fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()


# In[88]:


px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')


# In[ ]:




