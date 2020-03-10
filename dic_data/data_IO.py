import datetime
import os

import pickle as pick  # For data_save, data_load


def data_save_name(dictionary_name, filename):
    with open('save/data_' + filename + '.pkl', 'wb') as f:
        pick.dump(dictionary_name, f, pick.HIGHEST_PROTOCOL)
    print('Save complet as data_' + str(filename) + '.pkl - dic_length = ' + str(len(dictionary_name)))
    return 0


def data_load_name(filename):
    with open('save/' + filename, 'rb') as f:
        return pick.load(f)


def data_save(dictionary_name):
    datedata = datetime.datetime.utcnow()
    filename = datedata.strftime('%Y%m%d%H%M') + '-' + str(len(dictionary_name))
    data_save_name(dictionary_name, filename)
    return 0


def last_data_load():
    file_list = os.listdir('save/')
    if len(file_list) == 0:
        empty_dict = dict()
        return empty_dict
    file_list.sort()
    last_filename = file_list[len(file_list) - 1]
    print('Data load complete from data_' + str(last_filename))
    return data_load_name(last_filename)
