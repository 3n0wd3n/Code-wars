def reverse_words(text):
    new_str = ""
    words = text.split()
    counter = 0
    for char in text:
        if char == " ":
            counter += 1
    for word in words:
        if counter >= len(words):
            new_str += word[::-1] + " " + " "
        else:
            new_str += word[::-1] + " "
    if counter >= len(words):      
        return new_str[:-2]
    else:
        return new_str[:-1]
