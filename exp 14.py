import pandas as pd

data = {
    'customer_id': [1, 2, 3, 4, 5],
    'purchase_date': ['2023-07-05', '2023-08-12', '2023-08-02', '2023-08-15', '2023-07-25'],
    'age': [30, 25, 35, 28, 40]
}
sales_data = pd.DataFrame(data)

sales_data['purchase_date'] = pd.to_datetime(sales_data['purchase_date'])

current_date = pd.to_datetime('2023-08-27')
past_month_start = current_date - pd.DateOffset(months=1)
filtered_data = sales_data[(sales_data['purchase_date'] >= past_month_start) & (sales_data['purchase_date'] <= current_date)]

age_freq_dist = filtered_data['age'].value_counts().sort_index()

print(age_freq_dist)
