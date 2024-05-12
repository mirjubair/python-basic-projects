def analyze_text():
    # Get the filename from the user
    filename = input("Enter the filename with its extension (e.g., sample.txt): ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Calculate the number of characters including spaces
            char_count = len(text)
            
            # Calculate the number of words
            words = text.split()
            word_count = len(words)
            
            # Calculate the number of sentences by counting end punctuation
            sentence_count = text.count('.') + text.count('!') + text.count('?')
            
            # Get words to track frequencies and prepare the dictionary
            input_words = input("Enter words to track separated by commas (e.g., love,hate,joy): ")
            words_to_track = input_words.split(',')
            word_frequency = {word.strip().lower(): 0 for word in words_to_track}
            
            for word in words:
                word_lower = word.lower().strip(".,!?;:'\"()[]{}")
                if word_lower in word_frequency:
                    word_frequency[word_lower] += 1
            
            # Print the results
            print(f"\nCharacter Count (including spaces): {char_count}")
            print(f"Word Count: {word_count}")
            print(f"Sentence Count: {sentence_count}")
            print("Frequencies of specific words:")
            for word, frequency in word_frequency.items():
                print(f"{word}: {frequency}")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function to analyze text based on user input
if __name__ == "__main__":
    analyze_text()

