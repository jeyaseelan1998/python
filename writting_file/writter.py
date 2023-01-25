#!/usr/bin/env python3
def write_file (path, content):
  print("SELECT mode\nShould be r - read, w - write, a - append, r+ - both r & w")
  mode = input()
  if mode=='r':
   return
  with open(path, mode[0].lower()) as file:
    file.write(content)
  print("\u2713 File created successfully")

write_file("demo.txt", "Hello world!\nNext line\n\t--Jeyaseelan\n")
