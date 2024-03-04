#!/usr/bin/env python3

class MyString:
  
  def __init__(self,value=""):
    self.value = value 
  
    
        
        
        
  def is_sentence(self):
    ends_with_period = self.value.endswith(".")
    return ends_with_period 
   
  
  def is_question(self):
    ends_with_questionmark = self.value.endswith("?")
    return ends_with_questionmark
       
  def is_exclamation(self):
    ends_with_exclamation = self.value.endswith("!")
    return ends_with_exclamation 
  
  def count_sentences(self,value):
    
    if (type(value) in (value, str)):
      self._value = value
    else:
      print("The value must be a string.")
    
      # sentences = self.value.split(".")
      # count = 0 
      # for sentence in sentences:
      #   if sentence.strip() and (sentence.endswith("!")) or sentence.endswith("?") or sentence:
      #     count += 1
      # return count
      # print(count)
  
string = MyString()
string.value = "This is a string! It has three sentences. Right?"

string.count_sentences("This is a string! It has three sentences. Right?")

