def generate_hashtag(s):
    if s.isspace() or len(s) == 0:
        return False
    hshtg_str = "#"
    for idx, word in enumerate(s.split()):
        hshtg_str += word.lower().capitalize()

    if len(hshtg_str) > 140:
        return False
    return hshtg_str
