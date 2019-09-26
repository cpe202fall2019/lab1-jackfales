# Name: Jack Fales
# Course: CPE 202
# Instructor: Paul Hatalsky
# Assignment: Lab 1
# Term: Fall 2019

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None: # checks if int_list == None
      raise ValueError('List == None')
   if len(int_list) > 0: # if int_list is empty, return None
      max_value = int_list [0]
      for i in range(len(int_list)):
         if int_list [i] > max_value:
            max_value = int_list [i]
      return max_value
   return None

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None: # checks if int_list == None
      raise ValueError('List == None')
   if len(int_list) == 0:
      return []   # base case
   else:
      return [int_list[-1]] + reverse_rec(int_list[:-1]) # remove the last element and add it to the beginning

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError('List == None') # checks if int_list == None
   if len(int_list) == 0:
      return None
   if high >= low: # if low > high then binary search is complete
      mid = (low + high) // 2 # middle index of the search range
      if int_list [mid] == target: # if index matches, return index
         return(mid)
      elif target > int_list[mid]: # if target is greater than value checked, condense the range
         return(bin_search(target, mid + 1, high, int_list))
      else: 
         return(bin_search(target, low, mid - 1, int_list))
   return None # if target is not found return None

