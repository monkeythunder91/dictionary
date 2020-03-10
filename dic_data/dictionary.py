

def add_data(add_key, add_value, dictionary_name):
    if add_key in dictionary_name:
        return -1
    else:
        dictionary_name[add_key] = add_value
        return len(dictionary_name)

