import string
from collections import Counter

with open("customer_reviews.txt", "r") as file:
    reviews = file.read()

translator = str.maketrans("", "", string.punctuation)
processed_reviews = reviews.translate(translator).lower()

words = processed_reviews.split()

word_frequency = Counter(words)

print("Word Frequency Distribution:")
for word, frequency in word_frequency.most_common(10):  
    print(f"{word}: {frequency}")
