# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:14:13 2019

@author: Noel
"""

print("Select inputs any of the following 9 inputs for entering value into the game \n a01 \n a02 \n a03 \n a10 \n a11 \n a12 \n a21 \n a22 \n a23")

a=[["" for i in range(3)] for i in range(3)]
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
count=0
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
    user_input=input().split()
    if user_input ==["a00", "X"]:
        if a[0][0]=="X" or a[0][0]=="0":
           print( "Cell has a value")
        else:
            a[0][0]="X"
    if user_input == ["a01","X"]:
        if a[0][1]=="X" or a[0][1]=="0":
           print( "Cell has a value")
        else:
            a[0][1]="X"
    if user_input ==[ "a02","X"]:
        if a[0][2]=="X" or a[0][2]=="0":
           print( "Cell has a value")
        else:
            a[0][2]="X"
    if user_input ==[ "a10","X"]:
        if a[1][0]=="X" or a[1][0]=="0":
           print( "Cell has a value")
        else:
            a[1][0]="X"
    if user_input == ["a11","X"]:
        if a[1][1]=="X" or a[1][1]=="0":
           print( "Cell has a value")
        else:
            a[1][1]="X"
    if user_input ==[ "a12","X"]:
        if a[1][2]=="X" or a[1][2]=="0":
           print( "Cell has a value")
        else:
            a[1][2]="X"
    
    if user_input ==[ "a20","X"]:
         if a[2][0]=="X" or a[2][0]=="0":
            print( "Cell has a value")
         else:
            a[2][0]="X"
    if user_input ==[ "a21","X"]:
         if a[2][1]=="X" or a[2][1]=="0":
            print( "Cell has a value")
         else:
            a[2][1]="X"
    if user_input==["a22","X"]:
        if a[2][2]=="X" or a[2][2]=="0":
            print( "Cell has a value")
        else:
            a[2][2]="X"
    if user_input==["a00","0"]:
        if a[0][0]=="X" or a[0][0]=="0":
           print( "Cell has a value")
        else:
            a[0][0]="0"
    if user_input ==[ "a01","0"]:
        if a[0][1]=="X" or a[0][1]=="0":
           print( "Cell has a value")
        else:
            a[0][1]="0"
    if user_input == ["a02","0"]:
        if a[0][2]=="X" or a[0][2]=="0":
           print( "Cell has a value")
        else:
            a[0][2]="0"
    if user_input == ["a10","0"]:
        if a[1][0]=="X" or a[1][0]=="0":
           print( "Cell has a value")
        else:
            a[1][0]="0"
    if user_input ==[ "a11","0"]:
        if a[1][1]=="X" or a[1][1]=="0":
           print( "Cell has a value")
        else:
            a[1][1]="0"
    if user_input ==[ "a12","0"]:
        if a[1][2]=="X" or a[1][2]=="0":
           print( "Cell has a value")
        else:
            a[1][2]="0"
    if user_input == ["a10","0"]:
         if a[1][0]=="X" or a[1][0]=="0":
            print( "Cell has a value")
         else:
            a[1][2]="0"
    if user_input == ["a20","0"]:
         if a[2][0]=="X" or a[2][0]=="0":
            print( "Cell has a value")
         else:
            a[2][0]="0"
    if user_input == ["a21","0"]:
         if a[2][1]=="X" or a[2][1]=="0":
            print( "Cell has a value")
         else:
            a[2][1]="0"
    if user_input==["a22","0"]:
        if a[2][2]=="X" or a[2][2]=="0":
            print( "Cell has a value")
        else:
            a[2][2]="0"

    count+=1
    b=1
    if count>=3:        
        b=checK()
        print(a)
        if b==0:
           print(a)
           break
    if count>=9:
        print("Draw")
        break

print("I made Computer do it")



