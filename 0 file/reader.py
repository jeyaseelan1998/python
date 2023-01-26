#!/usr/bin/env python3

def reader (file_dir):
  result = {}
  with open(file_dir) as file:
    words = file.read().split()
    for word in words:
      if word.isalpha() and len(word)>3:
        if word not in result:
          result[word] = 0
        result[word] += 1
  return(result)

def display(result):
  for word, times in result.items():
    print("{:<9}|{:>2} times".format(word, times))
    print("-"*20)

result = reader("poem.txt")
display(result)
