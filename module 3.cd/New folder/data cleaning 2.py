import pandas as pd
import numpy as np
import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dmk@@522',
    database='car_data_project'
)

# Step 2: Load data from MySQL
df = pd.read_sql("SELECT * FROM cars_clean", conn)

# Step 3: Calculate statistics
stats = {
    'mean_price': df['product_price'].mean(),
    'median_price': df['product_price'].median(),
    'mode_price': df['product_price'].mode()[0],
    'std_dev_price': df['product_price'].std(),
    'variance_price': df['product_price'].var(),
    'min_price': df['product_price'].min(),
    'max_price': df['product_price'].max(),
    'range_price': df['product_price'].max() - df['product_price'].min(),

    'mean_milage': df['milage'].mean(),
    'median_milage': df['milage'].median(),
    'std_dev_milage': df['milage'].std(),
    'min_milage': df['milage'].min(),
    'max_milage': df['milage'].max()
}

# Step 4: Print to terminal
print("\n📊 Car Data Statistics Summary:")
for key, value in stats.items():
    print(f"{key}: {value}")

# Step 5: Save statistics to MySQL
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS car_stats_summary (
        stat_name VARCHAR(50) PRIMARY KEY,
        stat_value DOUBLE
    )
""")

# Clear existing records
cursor.execute("DELETE FROM car_stats_summary")

# Insert cleaned stats
for stat, value in stats.items():
    if pd.isna(value):
        value = None
    elif isinstance(value, (np.integer, np.int64)):
        value = int(value)
    elif isinstance(value, (np.floating, np.float64)):
        value = float(value)

    cursor.execute(
        "INSERT INTO car_stats_summary (stat_name, stat_value) VALUES (%s, %s)",
        (stat, value)
    )

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("\n✅ Statistics saved into 'car_stats_summary' table in MySQL!")
