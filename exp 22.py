import pandas as pd
import numpy as np
from scipy.stats import norm
data = pd.read_csv("C:/Users/user/OneDrive/Desktop/Fods/customer_reviews.csv")
print(data.head())
average_rating = data['rating'].mean()
print("Average Rating:", average_rating)
standard_error = data['rating'].std() / np.sqrt(len(data))
confidence_level = 0.95
z_score = norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_score * standard_error
confidence_interval_lower = average_rating - margin_of_error
confidence_interval_upper = average_rating + margin_of_error
print("Confidence Interval:", (confidence_interval_lower, confidence_interval_upper))
