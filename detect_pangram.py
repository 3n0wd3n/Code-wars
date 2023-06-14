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
