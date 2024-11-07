# E-commerce Analysis Project

This project presents an in-depth analysis of an e-commerce dataset from Google BigQuery's public dataset, [The Look E-commerce Dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=thelook_ecommerce&page=dataset&project=%3F&ws=!1m4!1m3!3m2!1sbigquery-public-data!2sthelook_ecommerce). The analysis aims to uncover insights into sales performance, customer behavior, geographic distribution, and traffic source effectiveness.

## Data Source

- **Dataset**: The Look E-commerce Dataset
- **Location**: Available publicly on Google BigQuery
- **Link**: [The Look E-commerce Dataset on BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=thelook_ecommerce&page=dataset&project=%3F&ws=!1m4!1m3!3m2!1sbigquery-public-data!2sthelook_ecommerce)

### Data Processing Steps

1. **Data Import**: The dataset was accessed through BigQuery and imported into Power BI for analysis.
2. **Data Cleaning**: 
   - Handled missing values and ensured data consistency across all tables.
   - Standardized data types, particularly for date fields and numerical values, to enable accurate calculations and comparisons.
   - Removed duplicates to maintain data integrity.
3. **Data Optimization**: 
   - Created a Date Table in Power BI for efficient time-based analysis.
   - Established relationships between tables (e.g., `users`, `orders`, `order_items`, `products`) to enable seamless data exploration.

---

## Dashboard Descriptions

### 1. **Country Analysis Dashboard**

   ![Country Analysis Dashboard]<img width="1232" alt="Screenshot 2024-11-07 at 15 36 04" src="https://github.com/user-attachments/assets/2c2a2aaa-94b6-4a08-958f-d30a744e761a">


   **Purpose**: To analyze the distribution of customers across different countries, states, and cities, highlighting popular regions.

   - **Top States**: Bar chart showing states with the highest number of visits.
   - **Most Visited Countries**: Pie chart to display the share of each country.
   - **Most Visited Cities**: List of cities with the highest visitor count.
   - **Map Visualization**: Provides a geographical view of customer locations.
   - **Filters**: Allows filtering by gender and date to view regional data for specific segments.

### 2. **Gender Analysis Dashboard**

   ![Gender Analysis Dashboard]!<img width="1246" alt="Screenshot 2024-11-07 at 15 36 11" src="https://github.com/user-attachments/assets/433d7cba-6532-455c-8e0c-dac23d3b4b64">



   **Purpose**: To compare customer spending and behavior across genders.

   - **Total Spending by Gender**: Bar chart comparing total sales by gender.
   - **Average Age by Gender**: Line chart showing age trends for each gender over time.
   - **User Base by Age Group and Gender**: Stacked area chart comparing age distribution across genders.
   - **Gender Distribution**: Pie chart summarizing the gender split among customers.
   - **Table Summary**: Shows breakdown of traffic sources by gender.
   - **Filters**: Gender and country filters to refine the view.

### 3. **Sales Performance Dashboard**

   ![Sales Performance Dashboard]<img width="1248" alt="Screenshot 2024-11-07 at 15 36 18" src="https://github.com/user-attachments/assets/5e620917-74f4-44d5-a96d-8546905ba47f">


   **Purpose**: To analyze sales trends, top-performing products, and category performance.

   - **Top Products**: Bar chart showing products with the highest sales.
   - **Sales by Category**: Pie chart of sales contribution by product category.
   - **Sales by Day of Week**: Bar chart showing sales volume on each day of the week.
   - **Key Metrics**: KPIs displaying total sales, total orders, and average order value.
   - **Filters**: Options to filter by order status, gender, and date.

### 4. **Traffic Source Analysis Dashboard**

   ![Traffic Source Analysis Dashboard]<img width="1246" alt="Screenshot 2024-11-07 at 15 36 25" src="https://github.com/user-attachments/assets/12006961-a106-43f0-9724-4b815ac35def">


   **Purpose**: To identify which traffic sources bring in the most profitable and repeat customers.

   - **Total Sales per Traffic Source**: Bar chart for revenue by traffic source.
   - **Repeat Customers by Traffic Source**: Bar chart showing customer loyalty per source.
   - **Average Order Value by Traffic Source**: Bar chart for average order size per source.
   - **Traffic by Gender**: Pie chart showing the breakdown of traffic sources by gender.
   - **Detailed Table**: Lists total sales and order counts by traffic source and country.
   - **Filters**: Allows filtering by gender, order status, and date to understand the impact of traffic sources on different customer segments.

---

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Power BI File**: Open `Ecommerce_Analysis.pbix` in Power BI Desktop to interact with the dashboards.
3. **Dataset**: If you want to explore further, you can access the dataset directly on BigQuery using the link provided above.

---

## Insights and Findings

1. **Country Analysis**: Helps identify key customer regions and potential areas for regional marketing.
2. **Gender Analysis**: Highlights differences in spending and age demographics between male and female customers, aiding in gender-targeted campaigns.
3. **Sales Performance**: Provides insights into top products, best-performing categories, and sales trends, supporting inventory and sales strategies.
4. **Traffic Source Analysis**: Identifies the most profitable traffic sources and which sources bring in loyal, repeat customers, informing marketing budget allocation.

---

## Project Structure

- **Power BI File**: `Ecommerce_Analysis.pbix` - The main Power BI dashboard file.
- **Screenshots**: A folder containing screenshots for each dashboard (e.g., `Country_Analysis.png`, `Gender_Analysis.png`, etc.).
- **README.md**: Project documentation explaining each dashboard and the analysis process.

---

## Contributing

Feel free to fork this project and submit pull requests if you’d like to contribute additional features, insights, or improvements.

## License

This project is open-source and available under the MIT License.

---

