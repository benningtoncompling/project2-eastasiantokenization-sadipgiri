#!/usr/bin/env python3

'''
    accuracy.py - Python3 program to return accuracy of Word Segmentation comparing tow files:
        i.e. (1)gold standard file with (2)segmented files
        NOTE: it matches each line of those two files and returns the accuracy percentage of our Word Segmentation (e.g. MaxMatch algorithm)
    Auhtor: Sadip Giri (sadipgiri@bennington.edu)
    Date: 12th March, 2019
'''

def accuracy(user_file='sadip_out.txt', gold_standard_file='gold_standard.txt'):
    '''
        - read user file
        - read gold standard file
        - count all lines that matches 
        - return percentage
    '''
    num_matched_lines = 0
    with open(user_file, 'r') as user_file:
        with open(gold_standard_file, 'r') as gold_standard_file:
            user_lines = user_file.readlines()
            gold_standard_lines = gold_standard_file.readlines()
            for user_line in user_lines:
                for gold_line in gold_standard_lines:
                    if user_line == gold_line:
                        num_matched_lines += 1
    return (num_matched_lines/len(user_lines)) * 100

if __name__ == '__main__':
    print(accuracy())
    
