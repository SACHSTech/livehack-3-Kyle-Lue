"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  determine when the total distance surpassed 100km and the average distance per day
 
Author: Lue.Kyle
 
Created:  03/02/2021
------------------------------------------------------------------------------
"""
print ("****** Welcome to the DoorDash Distance Tracker ******")

total_distance = 0
total_days = 0

print ("** Travel Log **")
distance_per_day = int(input("Enter the distance travelled for the day: "))
while total_distance > 100:
  distance_per_day = int(input("Enter the distance travelled for the day: "))
  total_distance = int(total_distance)+int(distance_per_day)
  total_days = total_days + 1
  
if total_distance < 100:
  print ("** Summary **")
  print ("It took " + str(total_days) + " to surpass 100km driven")
  average_distance = total_distance/total_days
  print ("The average distance travelled per day is " + str(average_distance) + " km")
