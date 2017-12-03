# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of enumerated types

from enum import Enum

Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

chosen_day = raw_input("\nWhat is your favorite day? ")

def favorite_day_and_number():
    day_counter = 1
    print ("Your favorite day is " + chosen_day + ".") 
    for a_day in Days:
        if chosen_day == str(a_day):
            print("\nThe corresponding number for that day in the week is: ")
            print(day_counter)
        else:
            day_counter = day_counter + 1
            
if chosen_day in Days:
    favorite_day_and_number()
else:
    print("\nThat's not a day.")     
    
    chosen_day = raw_input("Please enter your favorite day: ")
    favorite_day_and_number()
    print("")
