Business Requirement Document (BRD)
🧩 1. Business Problem
The goal is to analyze used car sales data to:

Understand pricing trends by fuel type, model year, and mileage

Identify key insights that influence car resale value

Prepare data for future predictive modeling (e.g., price prediction model)

Stakeholders are interested in:

Data-driven pricing recommendations

Insights by city, fuel type, and car specs

Structured reporting from raw online datasets

📥 2. Data Collection
Source: Kaggle Dataset – muhammadharis541/cars-datasets

Format: CSV file with car listings, including:

product_price (e.g., “PKR 42.5 lacs”)

model (e.g., 2022)

milage, fuel_type, engine, car_type, city_name, etc.

Storage:

Raw data imported into MySQL under schema: car_data_raw, table: cars_raw

🧹 3. Data Cleaning
Performed in Python (Pandas) after reading from MySQL:

Raw Column	Cleaned As	Description
model	year	Converted to integer car year
product_price	product_price	Cleaned PKR text, commas, converted to numeric (PKR)
milage	milage	Extracted digits, converted to integer
fuel_type	(unchanged)	Used for grouping insights
Others	(dropped or retained)	Non-essential columns were omitted from analysis

Missing values were dropped from core fields (year, milage, product_price) to ensure clean analysis.

🛠 4. Preparing Data
Cleaned DataFrame created in Python

Ready for:

Descriptive stats

Visualizations

Model building

(Optionally stored into MySQL under schema: car_data_project, table: cars_clean)

📊 5. Data Analysis & Statistics
Key statistics calculated:

Mean, Median, Mode for:

product_price

milage

year

Grouped insights:

Average price by fuel_type

Median mileage by year

Summary stats via .describe():

Min, max, standard deviation

💡 6. Insights Generated
Most common year of resale cars

Average price by fuel type

Relationship between mileage and selling price

Outliers in price or mileage distributions

🤖 7. (Next Step) Predictive Model
Regression model can be trained on:

Features: year, milage, fuel_type

Target: product_price

Potential to provide:

Price estimation for new listings

Recommendations for car purchases/sales

    




