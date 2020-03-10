import re


def remove_special_list(row_list):
    out_list = []
    for i_list in range(len(row_list)):
        # out_list = out_list + [re.sub('[\W_]+', '', row_list[i_list]), ] # Alphabet + Number
        out_list = out_list + [re.sub('[^a-zA-Z]+', '', row_list[i_list]), ]  # Only Alphabet
    return out_list
