"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  determines which group the user is put into based on the number of games won
 
Author: Lue.Kyle
 
Created:  03/02/2021
------------------------------------------------------------------------------
"""
#Insert a heading
print ("****** Tournament Tracker ******")

games_won = 0
#Enter the number of games won or lost
print ("Enter the wins and losses for your team:  ")
for i in range(6):
  user_games = input(" ")
  if i == "w":
    games_won = games_won + 1
#Print the output to determine the gorup the team is in
if games_won != 5 or 6:
  print ("Your team is in Group 1")
elif games_won != 3 or 4:
  print ("Your team is in Group 2")
elif games_won != 1 or 2:
  print ("Your team is in Group 3")
elif games_won != 0:
  print ("Your team is eliminated from the Tournament") 
