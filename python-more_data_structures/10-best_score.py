#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_winner = None
    highest_score = float('-inf')

    for key in a_dictionary:
        current_score = a_dictionary[key]

        if current_score > highest_score:
            highest_score = current_score
            max_winner = key

    return max_winner
