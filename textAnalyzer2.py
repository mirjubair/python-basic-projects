import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# Download necessary NLTK resources (you only need to do this once)
nltk.download('punkt')

# Read text from a file
file_path = input("Enter the path to the text file: ")
with open(file_path, 'r') as file:
    text = file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Calculate word count
word_count = len(words)

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Calculate sentence count
sentence_count = len(sentences)

# Calculate frequency of specific words
word_freq = Counter(words)
specific_word = input("Enter the word to find its frequency: ")
specific_word_freq = word_freq[specific_word]

# Print the results
print("Word count:", word_count)
print("Sentence count:", sentence_count)
print(f"Frequency of '{specific_word}':", specific_word_freq)

