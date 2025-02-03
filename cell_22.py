#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class node:
  def __init__(self):
    self.value = None
    self.ptr = None

  def add(self,i):
    self.value = input("Please enter value ")
    if i != size-1:
      self.ptr = i + 1
    else:
      self.ptr = None

def delete(start):
  if start == 0:
    llist[start].value = -1
    llist[start].ptr = -1
    start +=1
  else:
    llist[start].value = -1
    llist[start-1].ptr = llist[start].ptr
    start+=1


llist = []
size = int(input("please enter size of list "))
for i in range(0,size,1):
  llist.append(node())

start = -1
end = -1
free_pointer = 0
current_pointer = None
x = True
i = 0
while x:
  choice = input("Would you like to add or delete application from the queue (to exit, enter anything else) --- ")
  if choice == "add":
    if free_pointer == 0:
      print("Error")
    else:
      current_pointer = free_pointer
    llist[current_pointer].add(current_pointer)
    i+=1
  elif choice == "delete":
    delete(start) # makes a lot more sense to apply delete as a function rather than a method
  else:
    break

for i in range(0,size,1):
  while llist[i].value != -1:
    print(str(llist[i].value) + "    " + str(llist[i].ptr))

