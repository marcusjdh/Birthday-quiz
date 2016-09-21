"""
birthday.py
Author: Marcus Helble
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
user=input("Hello, what is your name?")
month=input("Hi " + user + ", what was the name of the month you were born in?")
year=input("And what year were you born in, " + user + " ?")
day=input("And the day?")


if month in  ["December", "January", "February"]:
    season = "winter"
else:
        if month in ["March", "April", "May"]:
            season = "spring"
        else: 
                if month in ["September", "October", "November"]:
                    season = "fall"
                else:
                    if month in ["June", "July", "August"]:
                        season = "summer"
monthname=["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
g=monthname.index("September")

if year in ["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989"]:
    gen = "Eighties"
else: 
        if year in ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"]:
             gen = "Nineties"
        else:
                  if int(year) >= 2000:
                    gen = "stone age"
                  
if month == "October" and int(day) == 31:
    print("You were born on Halloween!")
else:
    if g==todaymonth and int(day) == todaydate:
        print("Happy birthday!")
    else:
         print(user + ",  you are a " + season + " baby of the " + gen)



