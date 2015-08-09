#DEMO "BRAG!" — A BASIC program from the past.

#declare blank strings

firstname = ""
lastname = ""
answer = ""

#inroduction

print("Hello! I am a program written in Python!")
print("I would like to show you a few things that a Python program can do!\n")
print("First, I need some information.")
print("Tell me your first name. Press ENTER after you type it.")
print

#ask for name, make sure there's an answer

while firstname == "":
    firstname = input('Enter your first name: ')
if firstname == "":
    print("Now, cut that out!")

while lastname == "":
    lastname = input('And your last name: ')
if lastname == "":
    print("Now, cut that out!")

#piece answers together for full name and pull name length info

wholename = firstname + " " + lastname
lenfirst = len(firstname)
lenlast = len(lastname)
lenwhole = len(wholename)

#count letters in name

print("\nWell hello, " + wholename + "! That's a very nice name!")
print
print("Did you know that there are", lenfirst, "letters in your first name and", lenlast, "letters in your last name? That makes", lenfirst + lenlast, "letter in all!!!")
print

#ask if user wants to see name backwards and don't take no for an answer

print("\nWould you like to see your name printed backwards?")

while answer[: 1] != "y" and answer[: 1] != "Y":
    answer = input('Type yes or no: ')
    if answer[: 1] == "n" or answer[: 1] == "N":
        print("Please, let me show off for you!")
    if answer == "":
        print("I need an answer, please.")

i = lenwhole

print
print

#print name backwards with a quarter of a second wait for each letter displayed

import time
while i > 0:
    print(wholename[i - 1: i], end = "")
    i = i - 1
    time.sleep(.25)

print(end = '\n')

#ask for user's birthdate

print("\nNow, tell me your birthdate.")
month = int(input('First, the number of the month (1-12): '))
day = int(input('Next, the day: '))
year = int(input('And finally, the year: '))

#calculate difference between birthday and today, in days

import datetime
today = datetime.date.today()
someday = datetime.date(year, month, day)
diff = someday - today

t = (abs(diff.days))

print("\nI bet you didn't know that you are exactly", t, "days old!")

print("\nPress Enter to continue,", firstname, end='')
print(".")

input("...")

#make 'em read like it's 1983!

print("\n\nAs you can tell by this program, a computer programmed with Python")
print("is able to do many different things. It can count the letters in")
print("your name; it can remember the letters in your name and print them")
print("in reverse order; and, of course, it can do mathematical calculations")
print("like figuring out how many days old you are. It is")
print("important that you realize, however, that everything that")
print("happened was a result of a series of instructions (a program)")
print("written by a person. Soon you will be writing your own programs!")
print("\nBest of luck!")
print("\nNow,", firstname, end='')
print(", please continue to the next lesson.")
