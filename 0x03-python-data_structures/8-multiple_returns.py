#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        #if sentence is not empty
        first_char = sentence[0]
        #get length
    sentence_len = len(sentence)

    tuple_return = (sentence_len, first_char)
    return (tuple_return)
