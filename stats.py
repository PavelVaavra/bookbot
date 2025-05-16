def word_counter(s):
    return len(s.split())

def char_counter(s):
    res = {}
    for char in s:
        if char.lower() in res:
            res[char.lower()] += 1
        else:
            res[char.lower()] = 1
    return res