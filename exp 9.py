import pandas as pd

property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'num_bedrooms': [3, 4, 2, 5, 3],
    'area_sqft': [1800, 2200, 1500, 2800, 1900],
    'listing_price': [250000, 320000, 180000, 420000, 280000]
})

average_price_by_location = property_data.groupby('location')['listing_price'].mean()

num_properties_more_than_4_bedrooms = property_data[property_data['num_bedrooms'] > 4].shape[0]

property_largest_area = property_data.loc[property_data['area_sqft'].idxmax()]

print("Average listing price of properties in each location:")
print(average_price_by_location)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_4_bedrooms)
print("\nProperty with the largest area:")
print(property_largest_area)
