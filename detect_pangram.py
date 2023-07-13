"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string

def is_pangram(s):
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    for char in s:
        alphabet[char.lower()] = 1
        
    isPangram = True
    for char in alphabet:
        if alphabet[char] == 0:
           isPangram = False
           break
            
    return isPangram
