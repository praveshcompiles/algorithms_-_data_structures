import os
from collections import Counter 
import re

# Dictionary and counter in Python to find winner of election

def winner(input): 
  
     # convert list of candidates into dictionary 
     # output will be likes candidates = {'A':2, 'B':4} 
     votes = Counter(input) 
       
     # create another dictionary and it's key will 
     # be count of votes values will be name of  
     # candidates 
     dict = {} 
  
     for value in votes.values(): 
  
          # initialize empty list to each key to  
          # insert candidate names having same  
          # number of votes  
          dict[value] = [] 
  
     for (key,value) in votes.iteritems(): 
          dict[value].append(key) 
  
     # sort keys in descending order to get maximum  
     # value of votes 
     maxVote = sorted(dict.keys(),reverse=True)[0] 
  
     # check if more than 1 candidates have same  
     # number of votes. If yes, then sort the list 
     # first and print first element 
     if len(dict[maxVote])>1: 
         print sorted(dict[maxVote])[0] 
     else: 
         print dict[maxVote][0] 


# Functions to reverse a string 

def reverse(string): 
    string = string[::-1] 
    return string 

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


# Function to return a string after removing poison characters (eg. "aeiou" are poison chars here)
def removeStr():
    input = "Battle of the Vowels: Hawaii vs. Grozny"
    str = "aeiou"

    list_of_chars = list(input)
    pois = list(str)
    flags = [False] * 500
    for each in pois:
        flags[ord(each)] = True

    result = ''
    for char in list_of_chars:
        if flags[ord(char)] == False:
            result += char

    print(result)

# Reverse words in a string

def reverse():
    input = "Do or do not, there is no try."
    list_of_w = input.split()
    counter = len(list_of_w) - 1
    result = [''] * len(list_of_w)
    for word in list_of_w:
        result[counter] = word
        counter -= 1
    print(result)


# Missing number in an array
def getMissingNo(A): 
    n = len(A) 
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 


# Use of Regular Expression
def regularEx():
	regex = r"([a-zA-Z]+) (\d+)"
	match = re.search(regex, "I was born on June 24") 
	if match != None: 
		# this will print "June 24" 
		print "Full match: %s" % (match.group(0))

	    # this will print "June" 
	    print "Month: %s" % (match.group(1)) 

	    # this will print "24" 
	    print "Day: %s" % (match.group(2)) 
	else:
		print "The regex pattern does not match."


# function to check if two strings are 
# anagram or not  
def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.") 


# 2nd smallest number in an array
def print2Smallest(arr): 
  
    # There should be atleast two elements 
    arr_size = len(arr) 
    if arr_size < 2: 
        print("Invalid Input")
        return
  
    first = second = sys.maxint 
    for i in range(0, arr_size): 
  
        # If current element is smaller than first then 
        # update both first and second 
        if arr[i] < first: 
            second = first 
            first = arr[i] 
  
        # If arr[i] is in between first and second then 
        # update second 
        elif (arr[i] < second and arr[i] != first): 
            second = arr[i]; 
  
    if (second == sys.maxint): 
        print("No second smallest element")
    else: 
        print('The smallest element is', first,'and second smallest element is',second)


# Two Sum in a list
def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i



# Check if two strings are permutations of each other

def is_permutation(s1, s2): # in this case spaces count and character comparison is case insensitive
    if len(s1) != len(s2):
        return False
    char_count = [0 for _ in range(256)] # assume ASCII extended
    for c in s1:
        char_count[ord(c)] += 1
    for c in s2:
        char_count[ord(c)] -= 1
        if char_count[ord(c)] < 0:
            return False
    return True


# Check if a string is a rotation of another string
def is_substring(s1, s2):
    return s1 in s2


def string_rotation(s1, s2):
    return is_substring(s2, s1 + s1)