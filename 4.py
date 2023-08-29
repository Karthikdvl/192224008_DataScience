import numpy as np
sales_data = np.array([20000, 25000, 19000, 26000])

total_sales = np.sum(sales_data)

Q1_sales = sales_data[0]
Q4_sales = sales_data[3]
percentage_increase = ((Q4_sales - Q1_sales) / Q1_sales) * 100

print("Total sales for the year:", total_sales)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase, "%")
