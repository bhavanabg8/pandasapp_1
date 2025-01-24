# query = "cat dog cat dog mouse cat mouse dog"

# lst = query.split()

# unique_lst = sorted(list(set(lst)))

# print(unique_lst)

# index_lst = []
# # dt = {}
# for kw in unique_lst:
#     dt = {}
#     freq = lst.count(kw)
#     dt[kw] = freq
#     index_lst.append(dt)
# 
# print(index_lst)

# final_lst = [x for x in ]
# print(final_lst)
# for i, j in dt.items():

# print(sorted(dt.values()))


# lst = [x for x in range(5)]
# print(lst)

# for i in lst:
#     func(i)
#     print(i)


# import random

# var = random.random()
# print(var)

# def random_func():
    # x = random.random()
    # print(x)
    # return x

# while random_func() < 0.5:
#     print('bhavana')

# def addition(a,b):
#     c = a+b
#     return c

# added_value = addition(2,3)
# print(added_value) 

# def division(added_number):
#     d = added_number / 2
#     return d

# def multi(a,b,c):
#     m = a*b*c
#     return m

# def main(a, b):
#     added_value = addition(a,b)
#     divided_value  = division(added_number=added_value)
#     m = multi(a,b,divided_value)
#     return int(m)

# print(main(5,5))

# for i in range(3):
#     print(main(i, i))

# x=mutli(2,3,)
# print(x)

import pandas as pd

df = pd.read_csv("c:/Users/Acer/Documents/Supermart_dataset.csv") 

print(df.head())

print(df.info())

print(df.describe())

print(f"Total_Orders: {df['Order ID'].nunique()}")
# print("Total Orders:", df['Order ID'].nunique())
# print("Total_orders: " + str(df['Order ID'].nunique))
total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_discount = df["Discount"].sum()

print(f"Total_Sales: {total_sales}")

print(f"Total_Profit: {total_profit}")

print(f"Total_Discount: {total_discount}")

print(df.loc[df['Sales'] > 1000])

category_analysis = df.groupby("Category")[["Sales","Profit"]].sum()
print(category_analysis)

Region_Sales = df.groupby("Region")["Sales"].sum()
print(Region_Sales)

avg_discount = df.groupby("Sub Category")["Discount"].sum()
print(avg_discount)

high_profit_orders = df[df["Profit"] > 500]
print(high_profit_orders)

city_orders = df[df["City"] == "Chennai"]
print(city_orders)

fruits_veggies_orders = df[df["Category"] == "Fruits & Veggies"]
print(fruits_veggies_orders)

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month

df["Date"] = df["Order Date"].dt.date

Sales_by_year = df.groupby("Year")["Sales"].sum()
print(Sales_by_year)

Sales_by_month = df.groupby(["Year", "Month"])["Sales"].sum()
print(Sales_by_month)

import matplotlib.pyplot as plt
import seaborn as sns

category_analysis.plot(kind='bar', figsize=(8,6))
plt.title('Sales and Profit by Category')
plt.ylabel('Amount')
plt.show()

Region_Sales.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Monthly Sales Trend')
plt.ylabel('')
plt.show()

Sales_by_month.unstack(level=0).plot(kind='line', figsize=(12,6))
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Year')
plt.show()

df['Profit Margin'] = (df['Profit']/df['Sales'])* 100
top_profitable_orders = df.sort_values(by='Profit', ascending=False).head(5)
print(top_profitable_orders)

profitable_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(profitable_category)

correlation_matrix = df [['Sales', 'Profit', 'Discount']].corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm') 
plt.title('Correlation Matrix')
plt.show()

df.to_csv('processed_data.csv', index=False)

missing_values = df.isnull().sum()
print("Missing Values\n", missing_values)

sns.heatmap(df.notnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()







