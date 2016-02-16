#!/usr/bin/python3.4
# coding: utf8
import sys
import random
class NewWord():
    """Class creating a new word"""
    def __init__(self, shortest_word, longest_word, random_1, chce_frst_ltr):
        """Initializing word"""
        self.size = random.randrange(shortest_word, longest_word)
        i = 0
        while i < len(chce_frst_ltr):
            if random_1 <= chce_frst_ltr[i][1]:
                self.first_letter = chce_frst_ltr[i][0]
                break
            i += 1
    def create_word(self, chance_after_letter, chce_frst_ltr, doubling_letter_chance):
        """Creating the word"""
        i = 0
        final_word = str()
        final_word += self.first_letter
        while i < (self.size - 1): # -1 cause of first letter
            random_number = random.randrange(100)
            g = 0
            while g < len(chance_after_letter[final_word[i]]):
                if random_number <= chance_after_letter[final_word[i]][g][1]:
                    final_word += chance_after_letter[final_word[i]][g][0]
                    if(chance_after_letter[final_word[i]][g][0] in doubling_letter_chance) and (random.randrange(100) <= doubling_letter_chance[chance_after_letter[final_word[i]][g][0]]):
                        final_word += chance_after_letter[final_word[i]][g][0]
                        i += 1
                    break
                g += 1
            i += 1
        # final_word = final_word.replace(' ', '')
        return final_word
