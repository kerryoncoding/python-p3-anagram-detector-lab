# your code goes here!

class Anagram:
   def __init__(self, word):
      self.word_sorted = sorted([letter for letter in word])
   
   def match(self, check_list):
      match_check_list = []

      for item in check_list:
         if sorted([letter for letter in item]) == self.word_sorted:
            match_check_list.append(item)
         
      return match_check_list
   
   



