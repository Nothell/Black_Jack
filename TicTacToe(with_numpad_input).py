# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:29:54 2019

@author: Noel
"""
#Taking Input from Player1
print("Welcome to Tic Ta Toe")
print("Player1 Please choose X or Y:")
player1=input()
player2="X"
if player1=="X":
    player2="0"
else:
    player1="0"
    
#Initializing b as an  empty list    
b=[" "," "," "," "," "," "," "," "," "]   

#Function to check the Basic logic of tic tac toe
def check(winner):
    if b[0]==b[4]==b[8]==winner:
        return winner
    if b[0]==b[1]==b[2]==winner:
        return winner
    if b[0]==b[3]==b[6]==winner:
        return winner
    if b[1]==b[4]==b[7]==winner:
        return winner
    if b[2]==b[5]==b[8]==winner:
        return winner
    if b[3]==b[4]==b[5]==winner:
        return winner
    if b[6]==b[7]==b[8]==winner:
        return winner
    if b[2]==b[4]==b[6]==winner:
        return winner
    
#Count variable to count the while loop once so that first input comes to Player1    
count=0
#Function which allows Players to Replay. It also resets the Game
def replay_choice():
       print("Do you want to replay the game")   
       winner_input=input()
       if winner_input=="yes":
                for i in range(9):
                    b[i]=" "
                
                return "yes"
    
#Fucntion to check if the Player inserts into already filled cell
def check3():
    check_empty=0
    for i in range(9):
        if b[i]=="X" or b[i]=="0":
            check_empty+=1
            if check_empty==9:
                return 1
            else:
                continue
           
#Function whihc displays Board
def Board():
    
    print(" "*2+b[6]+""*1+"|"+""*1+" "*2+b[7]+""*1+"|"+""*1+" "*2+b[8]+""*1)
    print(" "*2+b[3]+""*1+"|"+""*1+" "*2+b[4]+""*1+"|"+""*1+" "*2+b[5]+""*1)
    print(" "*2+b[0]+""*1+"|"+""*1+" "*2+b[1]+""*1+"|"+""*1+" "*2+b[2]+""*1)
  
#Variable stores the returned value from the check function
store1=0
store2=0   
store3=0
store=0
while True:
    Board()  
       
    if count==1:
           opponent2=int(input())
           if b[opponent2-1]=="X" or b[opponent2-1]=="0":
               print("You cannot enter here, position is already taken")
               opponent2=int(input())
           else:
               b[opponent2-1]=player2
               Board()
               store1=check(player2)              
               if store1==player2:
                      Board()
                      print("Player2 wins")
                      store=replay_choice()
                      if store != "yes":
                            break
                      else:
                          continue
    
    opponent1=int(input())
    if b[opponent1-1]=="X" or b[opponent1-1]=="0":
               print("You cannot enter here,position is already taken")
    else:
         b[opponent1-1]=player1
         store2=check(player1)
         if store2==player1:
              Board()
              print("Player1 wins")
              store=replay_choice()
              if store != "yes":
                     break
    store3=check3()
    if store3==1:
        print("Draw")
        Board()
        break
    count=1    
    
