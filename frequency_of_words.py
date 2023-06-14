words = ["42", "IT", "Metro", "Universe", "Technology", "Time", "Time"]

def frequency_of_words(words):
    word_frequency = {}
    for word in words:
        if not word in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] = word_frequency.get(word) + 1
    return word_frequency
    
print(frequency_of_words(words))
