"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
"""

def pig_it(text):
    new_tense = ""
    txt = text.split()
    for idx, word in enumerate(txt):
        first_letter = word[0]
        word = word[1:]
        if len(word) == 0:
            if not first_letter in "?!" and len(word) == 0:
                word += first_letter + "ay" + " "
            if first_letter in "?!":
                word += first_letter
            new_tense += word
        else:
            word += first_letter + "ay" + " "
            new_tense += word
    if "?" in new_tense or "!" in new_tense:
        new_tense = new_tense[0:len(new_tense)]
    else:
        new_tense = new_tense[0:len(new_tense) - 1]
    return new_tense
