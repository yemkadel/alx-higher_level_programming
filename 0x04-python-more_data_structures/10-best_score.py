#!/usr/bin/python3
def best_score(a_dictionary):
    sorted_list = list(sorted(a_dictionary.items(), key=lambda item: item[1]))
    return sorted_list[0]
