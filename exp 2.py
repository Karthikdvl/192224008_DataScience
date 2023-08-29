import numpy as np

sales_data = np.array([
    [100, 150, 200],  
    [120, 180, 220], 
    [90, 160, 210]    
])

average_price = np.mean(sales_data)

print("Average Price of All Products:", average_price)
