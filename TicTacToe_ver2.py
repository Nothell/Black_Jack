# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:37:21 2019

@author: Noel
"""
a=[["" for i in range(3)]for i in range(3)]



for i in range(3):
    if i==0:
        for j in range(3):
            a[i][j]=j+1
    if i==1:
        for j in range(3):
            a[i][j]=j+4
    if i==2:
        for j in range(3):
            a[i][j]=j+7
print(a)

def checK():
    for i in range(3):
        if a[i][0]==a[i][1]==a[i][2]:
            return 0
        if a[0][i]==a[1][i]==a[2][i]:
            return 0
    for i in range(1):
        if a[i][i]==a[i+1][i+1]==a[i+2][i+2]:
            return 0
    for i in range(1):
        if a[i+2][i]==a[i+1][i+1]==a[i][i+2]:
            return 0






while True:
    user_input=[int(input()),int(input()),input()]
    
    if a[user_input[0]][user_input[1]]=="X" or a[user_input[0]][user_input[1]]=="0" :
                           print("Cell is filled")
    else:
        a[user_input[0]][user_input[1]]=user_input[2]
                    
                
               
    b=1
    b=checK()
    
    print(a)
    if b==0:
        print("Congrats you have won the Game")
        break
    count=0
    for i in range(3):
        
        for j in range(3):
            if a[i][j]=="X" or a[i][j]=="0":
                count+=1
                if count==9:
                    print("Draw")
                    break
                    
    
    
            
    
    
    
    
    
    