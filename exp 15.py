import pandas as pd


interaction_data = pd.DataFrame({
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [100, 150, 80, 200, 120, 70, 90, 180, 110, 160]
})

likes_frequency = interaction_data['likes'].value_counts().sort_index()

print("Frequency distribution of likes among the posts:")
print(likes_frequency)
