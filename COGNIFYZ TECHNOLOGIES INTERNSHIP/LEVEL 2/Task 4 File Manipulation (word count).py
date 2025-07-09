from collections import Counter

file_path = input("Enter file name: ")

with open(file_path, 'r', encoding='utf-8') as file:
    words = file.read().lower().split()

word_counts = Counter(words)

for word in sorted(word_counts):
    print(f"{word}: {word_counts[word]}")