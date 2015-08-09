print ("Hello! I am a program written in Python!")
print ("I would like to show you a few things that a Python program can do!\n")
print ("First, I need some information.")
print ("Tell me your first name. Press ENTER after you type it.")
print

firstname = ""
lastname = ""

while firstname == "":
    firstname = input ('Enter your first name: ')
    if firstname == "":
        print ("Now, cut that out!")
    
while lastname == "":
    lastname = input ('And your last name: ')
    if lastname == "":
        print ("Now, cut that out!")

wholename = firstname + " " + lastname
lenfirst = len(firstname)
lenlast = len(lastname)
lenwhole = len(wholename)

print ("\nWell hello, " + wholename + "! That's a very nice name!")
print
print ("Did you know that there are",lenfirst,"letters in your first name and",lenlast,"letters in your last name? That makes",lenfirst+lenlast,"letter in all!!!")
print

answer = ""

print ("\nWould you like to see your name printed backwards?")

while answer[:1] != "y":
    answer = input ('Type yes or no: ')

    if answer == "":
        print ("I need an answer, please.")
    if answer[:1] == "n":
        print ("Please, let me show off for you!")

i = lenwhole

print
print

import time
while i > 0:
    print (wholename[i-1:i], end="")
    i = i - 1
    time.sleep(.25)

print (end = '\n')

print ("\nNow, tell me your birthdate.")
month = int(input('First, the number of the month (1-12): '))
day = int(input('Next, the day: '))
year = int(input('And finally, the year: '))

if year > 1900:
    year = year - 1900
if year > 2000:
    year = year - 2000

y1 = 365 * (year - 1) + (year - 1) / 4 + 1

import time
import datetime

print ("\nToday's date is ", )

yearnow = int(datetime.date.today().strftime("%Y"))
monthnow = (datetime.date.today().strftime("%B"))
daynow = (datetime.date.today().strftime("%d"))


if year % 4 != 0:
    daysinmonth = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    daysinmonth = [31,28,31,30,31,30,31,31,30,31,30,31]

print (y1)
