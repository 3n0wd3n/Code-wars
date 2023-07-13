"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

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
