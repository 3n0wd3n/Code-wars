def disemvowel(string_):
    new_str = ""
    vowels = "aeiou"
    for char in string_:
        if not char.lower() in vowels:
            new_str += char 
    return new_str
