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

def sort_alpha_chars(char_dict):
    lst = []
    for item in char_dict:
        if item.isalpha():
            tmp = {}
            tmp["char"] = item
            tmp["num"] = char_dict[item]
            lst.append(tmp)
    lst.sort(reverse=True, key=lambda item: item["num"])
    return lst