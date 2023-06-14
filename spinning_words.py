def spin_words(sentence):
    words = sentence.split()
    new_sentence = ""
    for word in words:
        if len(word) > 4:
            new_sentence += word[::-1] + " "
        else:
            new_sentence += word + " "     
    return new_sentence[:-1]
