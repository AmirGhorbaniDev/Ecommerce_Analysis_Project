import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (assuming CSV files or replace with your data source)
users = pd.read_csv('users.csv')
orders = pd.read_csv('orders.csv')
order_items = pd.read_csv('order_items.csv')
products = pd.read_csv('products.csv')

# Set plot style
sns.set(style="whitegrid")

# 1. Total Sales by Traffic Source
total_sales_by_traffic_source = (
    orders.merge(order_items, on='order_id')
          .merge(users[['id', 'traffic_source']], left_on='user_id', right_on='id')
          .groupby('traffic_source')['sale_price']
          .sum()
          .sort_values(ascending=False)
)
print(total_sales_by_traffic_source)

# Plot Total Sales by Traffic Source
total_sales_by_traffic_source.plot(kind='bar', title='Total Sales by Traffic Source')
plt.ylabel('Total Sales')
plt.show()

# 2. Average Order Value by Traffic Source
avg_order_value_by_traffic_source = (
    orders.merge(order_items, on='order_id')
          .merge(users[['id', 'traffic_source']], left_on='user_id', right_on='id')
          .groupby('traffic_source')['sale_price']
          .mean()
          .sort_values(ascending=False)
)
print(avg_order_value_by_traffic_source)

# Plot Average Order Value by Traffic Source
avg_order_value_by_traffic_source.plot(kind='bar', title='Average Order Value by Traffic Source')
plt.ylabel('Average Order Value')
plt.show()

# 3. Repeat Customers by Traffic Source
repeat_customers = orders.groupby('user_id').size()
repeat_customers = repeat_customers[repeat_customers > 1].index
repeat_customers_by_traffic_source = (
    users[users['id'].isin(repeat_customers)]
    .groupby('traffic_source')
    .size()
)
print(repeat_customers_by_traffic_source)

# Plot Repeat Customers by Traffic Source
repeat_customers_by_traffic_source.plot(kind='bar', title='Repeat Customers by Traffic Source')
plt.ylabel('Number of Repeat Customers')
plt.show()

# 4. Total Sales by Gender
total_sales_by_gender = (
    orders.merge(order_items, on='order_id')
          .merge(users[['id', 'gender']], left_on='user_id', right_on='id')
          .groupby('gender')['sale_price']
          .sum()
)
print(total_sales_by_gender)

# Plot Total Sales by Gender
total_sales_by_gender.plot(kind='bar', title='Total Sales by Gender')
plt.ylabel('Total Sales')
plt.show()

# 5. Average Age by Gender
avg_age_by_gender = users.groupby('gender')['age'].mean()
print(avg_age_by_gender)

# Plot Average Age by Gender
avg_age_by_gender.plot(kind='bar', title='Average Age by Gender')
plt.ylabel('Average Age')
plt.show()

# 6. User Base by Age Group and Gender
age_bins = [0, 18, 25, 35, 45, 55, 100]
age_labels = ['<18', '18-25', '26-35', '36-45', '46-55', '55+']
users['age_group'] = pd.cut(users['age'], bins=age_bins, labels=age_labels)
user_base_by_age_gender = users.groupby(['age_group', 'gender']).size().unstack()
print(user_base_by_age_gender)

# Plot User Base by Age Group and Gender
user_base_by_age_gender.plot(kind='bar', stacked=True, title='User Base by Age Group and Gender')
plt.ylabel('Number of Users')
plt.show()

# 7. Top 5 Products by Sales
top_products = (
    order_items.merge(products, left_on='product_id', right_on='id')
               .groupby('name')['sale_price']
               .sum()
               .sort_values(ascending=False)
               .head(5)
)
print(top_products)

# Plot Top 5 Products by Sales
top_products.plot(kind='bar', title='Top 5 Products by Sales')
plt.ylabel('Total Sales')
plt.show()

# 8. Sales by Product Category
sales_by_category = (
    order_items.merge(products, left_on='product_id', right_on='id')
               .groupby('category')['sale_price']
               .sum()
)
print(sales_by_category)

# Plot Sales by Product Category
sales_by_category.plot(kind='bar', title='Sales by Product Category')
plt.ylabel('Total Sales')
plt.show()

# 9. Sales Trends by Month
orders['created_at'] = pd.to_datetime(orders['created_at'])
sales_trends_by_month = (
    orders.merge(order_items, on='order_id')
          .set_index('created_at')
          .resample('M')['sale_price']
          .sum()
)
print(sales_trends_by_month)

# Plot Sales Trends by Month
sales_trends_by_month.plot(title='Sales Trends by Month')
plt.ylabel('Total Sales')
plt.show()

# 10. Sales by Day of the Week
sales_by_day_of_week = (
    orders.merge(order_items, on='order_id')
          .assign(day_of_week=orders['created_at'].dt.day_name())
          .groupby('day_of_week')['sale_price']
          .sum()
)
print(sales_by_day_of_week)

# Plot Sales by Day of the Week
sales_by_day_of_week.plot(kind='bar', title='Sales by Day of the Week')
plt.ylabel('Total Sales')
plt.show()

# 11. Geographic Distribution of Customers by Country
customer_distribution_by_country = users['country'].value_counts()
print(customer_distribution_by_country)

# Plot Geographic Distribution of Customers by Country
customer_distribution_by_country.plot(kind='bar', title='Customer Distribution by Country')
plt.ylabel('Number of Customers')
plt.show()

# 12. Traffic Source Breakdown by Country
traffic_source_by_country = (
    orders.merge(order_items, on='order_id')
          .merge(users[['id', 'country', 'traffic_source']], left_on='user_id', right_on='id')
          .groupby(['country', 'traffic_source'])['sale_price']
          .sum()
          .unstack()
)
print(traffic_source_by_country)

# Plot Traffic Source Breakdown by Country
traffic_source_by_country.plot(kind='bar', stacked=True, title='Traffic Source Breakdown by Country')
plt.ylabel('Total Sales')
plt.show()
