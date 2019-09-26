# Name: Jack Fales
# Course: CPE 202
# Instructor: Paul Hatalksy
# Assignment: Lab 1 Test Cases
# Term: Fall 2019

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        one_element_list = [1]
        empty_List = []
        multi_element_list_ordered = [1, 2, 3]
        multi_element_list_unordered = [7, 3, 8, 10]
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter(one_element_list), 1) # used to check for a list with one element
        self.assertEqual(max_list_iter(multi_element_list_ordered), 3) # checks for multiple ordered elements
        self.assertEqual(max_list_iter(multi_element_list_unordered), 10) # checks for multiple unordered elements
        self.assertEqual(max_list_iter(empty_List), None) # checks for an empty list


    def test_reverse_rec(self):
        none_List = None
        single_List = [1]
        empty_List = []
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # standard case
        with self.assertRaises(ValueError): # used to check for exception
            reverse_rec(none_List)
        self.assertEqual(reverse_rec(single_List), [1]) # checks for a list of a single element
        self.assertEqual(reverse_rec(empty_List), []) # checks for an empty list


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        none_List = None
        empty_List = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # standard case if target is at mid
        with self.assertRaises(ValueError): # used to check for exception
            bin_search(4, 0, 2, none_List)
        self.assertEqual(bin_search(4, 0, 3, empty_List), None) # checks for an empty list
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5 ) # standard case if target is greater than mid
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 ) # standard case if target is less than mid


if __name__ == "__main__":
        unittest.main()

    
