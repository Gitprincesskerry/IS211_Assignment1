#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is Kerry Rainford's Week 1 Assignment Part 2"

class Book(Exception):
    def __init__(self, title, author):
        """An init function which has 2 instances (title and author) which are set to object variables"""
        self.author = author
        self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author +".")

b_a1 = Book("\"Of Mice and Men", "John Steinbeck\"")
b_a2 = Book("\"To Kill a Mockingbird", "Harper Lee\"")

b_a1.display()
b_a2.display()


