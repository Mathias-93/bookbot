def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_character(text):
    char_dict = {}

    for character in text:
        c = character.lower()
        if (c not in char_dict):
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]


def pretty_print(dict):
    
    dict_list = []

    for entry in dict:
        complete_entry = { "char": entry.lower(), "num": dict[entry] }
        dict_list.append(complete_entry)

    dict_list.sort(reverse=True, key=sort_on)

    for entry in dict_list:
        if(entry["char"].isalpha()):
            print(f"{entry["char"]}: {entry["num"]}")

