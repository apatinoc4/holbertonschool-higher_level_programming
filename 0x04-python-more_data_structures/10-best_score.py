#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        scores = []
        for k, v in my_dict.items():
            scores.append(v)
        scores.sort()
        high_score = scores[-1]
        for k, v in my_dict.items():
            if my_dict[k] is high_score:
                return k
    return None
