# -*- coding: utf-8 -*-
# @Author: Nitesh
# @Date:   2017-04-05 13:01:10
# @Last Modified by:   Nitesh
# @Last Modified time: 2019-07-02 16:05:12

import random
def choose_word(min_word_length):
    """Get a random word"""
    num_words_processed = 0
    current_word = None
    with open("wordlist.txt", 'r') as f:
        for word in f:
            word = word.strip().lower()
            if len(word) > min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                current_word = word
    return current_word
