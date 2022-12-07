#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {keys: x * 2 for keys in a_dictionary.keys() for x in a_dictionary.get(keys)}
    return new_dic
