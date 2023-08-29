import string
from collections import Counter

with open("sample_text.txt", "r") as file:
    text = file.read()

translator = str.maketrans("", "", string.punctuation)
processed_text = text.translate(translator).lower()

words = processed_text.split()

word_frequency = Counter(words)

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
