import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Loading Dataset
df=pd.read_csv('SampleSuperstore.csv')
print(df.head())

#Checking for null values if any
print(df.isnull().sum())

#Checking for duplicate data
df.duplicated().sum()
df.drop_duplicates()

#Comment: It is observed that the Country is same i.e United States for all rows. Thus, Country column can be ignored
del df['Country']
del df['Postal Code']
#print(df.head())

#To check unique values
print(df.nunique())

#Observing correlation in all the numeric columns
print(df.corr())

#Visualizing
plt.bar('Sub-Category','Category',data=df)

plt.xticks(rotation=45)
plt.show()

#From aboove plot we make out the number of sub categories in a particular category
#Most of the goods belong to office supply

df.hist(bins=50,figsize=(20,15))
plt.show()

#Conclusion: The plot is not normal its skewed

#Lets check which states get the most supply

sns.countplot(x=df['State'])
plt.xticks(rotation=90)
plt.show()

#It is observed that maximum goods is supplied to california

sns.set(style="whitegrid")
plt.figure(2, figsize=(20,15))
sns.barplot(x='Sub-Category',y='Profit', data=df, palette='Spectral')
plt.suptitle('Pie Consumption Patterns in the United States', fontsize=16)
plt.show()

#It is observed that copiers are making the maximum profit and no loss and max loss is incured by Tables

#Now lets see the discouts vs Profit

plt.figure(figsize=(10,4))
sns.lineplot(x='Discount',y='Profit', data=df , color='y',label='Discount')
plt.legend()
plt.show()



#Plotting Profit and Sales in each state
state_sale_profit = df.groupby('State')[['Sales','Profit']].sum()
state_sale_profit.sort_values('Sales', ascending = False, inplace=True)
print(state_sale_profit)

state_sale_profit.plot(kind = "bar", figsize=(25,12), color = ['darkviolet','dodgerblue'])
plt.title('Sales/Profit in each State')
plt.xticks(rotation = 90)
plt.xlabel('State')
plt.ylabel('Sales/Profit')
plt.show()



#Which Sub-Category is most ordered
f, ax = plt.subplots(1, 1, figsize=(15,4))
sns.countplot(x = df['Sub-Category'], order = df['Sub-Category'].value_counts().index, palette = 'plasma')
plt.title('Order Count by Sub-Category')
plt.xticks(rotation=90)
plt.xlabel('Sub-Category')
plt.ylabel('Orders')
plt.show()


#This now we which subcateory is most ordered and makes most profit and which makes loss
#Lets plot sales and profit ofeach sub-category

subcategory_sale_profit = df.groupby('Sub-Category')[['Sales', 'Profit']].sum()
subcategory_sale_profit.sort_values('Sales', ascending = False, inplace=True)
subcategory_sale_profit.plot(kind = "bar",color = ["rebeccapurple","mediumpurple"], figsize = (20,8))

plt.title('Sales/Profit in each Sub-Category')
plt.xlabel('Category')
plt.ylabel('Sales/Profit')
plt.show()

#Now lets see segment wise profit and loss incured

seg = df.groupby(['Sub-Category', 'Segment'])[['Quantity','Sales','Profit']].sum().reset_index()

sns.catplot(x='Sub-Category', y='Sales', hue = 'Segment', data = seg, kind='bar',palette='tab20c',aspect=2,height=8)
plt.title('Sub-Category Sales Segment-wise')
sns.catplot(x='Sub-Category', y='Profit', hue = 'Segment',data = seg, kind='bar',palette='tab20c',aspect=2,height=8)
plt.title('Sub-Category Profit Segment-wise')
plt.show()


#Now lets plot the Profit vs Discount

plt.scatter(df['Discount'], df['Profit'])
plt.title('Discount vs. Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.show()

#Conclusion Here for higher discounts the profit is lesser

#Lastly lets see what is the average profit
print(np.mean(df['Profit']))


#Conclusions
'''
1.Even though machines are most sold but It is observed that copiers are making the maximum profit and no loss and max loss is incured by Tables
2.Most profit is made in the consumer segment
3.Maximum supply is recieved in California, Hence it also makes the max profit
4.Office Supplies has the highest frequency of purchases. Technology has the most sales and is the most profitable. Furniture has the least profit although it has the second-highest sales.
5.The profit from Corporate segment is higher than that from Consumer segment.
6.Out of the top 10 states with the highest sales, 5 undergo an overall loss.Texas, which has the third-highest sales, witnesses the highest loss.
7.Conclusions are: a.More the sales More the profit
                   b.More the discount Less the profit
8.Overall the company is making averge profit of 28.65 which is very very less campared to the sales happening
9.Solution would be trying to reduce cost of production or reduce discounts where losses are high.
10. 
'''