Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> print ("Hello World")
Hello World
>>> a="Hello"
>>> b="World"
>>> a="Goodbye"
>>> print(a+b)
GoodbyeWorld
>>> a="abc123#$"
>>> print(a)
abc123#$
>>> print("abc")
abc
>>> type(a)
<class 'str'>
>>> a=1
>>> type(a)
<class 'int'>
>>> b=2
>>> print(a+b)
3
>>> a=2.5
>>> type(a)
<class 'float'>
>>> a=True
>>> a=False
>>> type(a)
<class 'bool'>
>>> not a
True
>>> a=True
>>> not a
False
>>> a=2.0
>>> type(a)
<class 'float'>
>>> a=int(a)
>>> type(a)
<class 'int'>
>>> print(a)
2
>>> 
======== RESTART: /Users/joecolonna/Documents/Python/Python practice.py ========
Please enter a test score: 

numberofscores = 0
score = 0
total = 0
average = 0
scorecount = 0
numberofscores = int (input("Please enter the number of scores you want to average"))
For score = int(input("please enter a score: "))
total = total + score
scorecount = scorecount + 1

average = total / numberofscores
print (average)
