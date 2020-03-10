import datetime, os

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

import dic_data as dc

span_classname = "one-click-content css-1p89gle e1q3nk1v4"

data_dictionary = dc.last_data_load()

word_count = 0

if len(os.listdir('save/')) == 0:
    print("no previous data")
    current_word = 'apple'
    html = urlopen("https://www.dictionary.com/browse/" + current_word)
    Object = BeautifulSoup(html, "html.parser")
    rowdata = Object.findAll("span", {"class": span_classname})
    degeneracy = []
    for i_list in range(len(rowdata)):
        degeneracy = degeneracy + [dc.remove_special_list(rowdata[i_list].text.split(' ')), ]
    dc.add_data(current_word, degeneracy, data_dictionary)

while True:
    current_word = 0
    dic_keys = list(data_dictionary.keys())
    for i_key in range(len(data_dictionary)):
        dic_value = data_dictionary[dic_keys[i_key]]
        for i_value in range(len(dic_value)):
            for i_second_value in range(len(dic_value[i_value])):
                if not dic_value[i_value][i_second_value] in dic_keys:
                    current_word = dic_value[i_value][i_second_value]
    if current_word == 0:
        print("no more words")
        break
    print(word_count,' -> ',current_word)
    try:
        html = urlopen("https://www.dictionary.com/browse/" + current_word)
    except HTTPError as e:
        print(str(current_word) + ' = HTTP Error')
        data_dictionary[current_word] = ''

    else:
        Object = BeautifulSoup(html, "html.parser")
        rowdata = Object.findAll("span", {"class": span_classname})
        degeneracy = []
        for i_list in range(len(rowdata)):
            degeneracy = degeneracy + [dc.remove_special_list(rowdata[i_list].text.split(' ')), ]
        dc.add_data(current_word, degeneracy, data_dictionary)
    word_count += 1

    if word_count > 100:
        dc.data_save(data_dictionary)
        word_count = 0
