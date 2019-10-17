# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:43:24 2019

@author: Noel
"""
import random
class record():
    def __init__(self,bet,balance):
        self.bet=bet
        self.balance=balance
    def __str__(self):
        return f"Your balance now is {self.balance}"
    def __add__(self,no):
        self.balance=self.balance+self.bet+no
    def __betplaced__(self):
       self.balance=self.balance-self.bet
   
    

         
class Player_hand():
    def __init__(self,player_card):
        self.player_card=player_card
    def __str__(self):
        return f"Your Cards are: {self.player_card}"
    def __hit__(self,no):
        self.player_card.append(no)
        
        
class Dealers_hand():
    def __init__(self,dealers_card):
        self.dealers_card=dealers_card
    def __str__(self,f=0):
        if f==0:
            return f"Dealers Face card: {self.dealers_card[0]}"
        if f==1:
            return f"Dealers Face card: {self.dealers_card}"
    def __hit__(self,no):
        self.dealers_card.append(no)
    
        
def randomgenerator():
    letter=[2,3,4,5,6,7,8,9,10,"K","Q","J","A"]
    x=random.choices(letter,k=2)
    y=random.choices(letter,k=2)
    return x,y
        

def Calculate(x,y):
    d=0
    c=0
    e=0   
    f=0
    
    x=[10 if x[i] in ["K","J","Q"] else x[i] for i in range(len(x))]
    y=[10 if y[i] in ["K","J","Q"] else y[i] for i in range(len(y))]
    
    z=[1 if x[i]=="A" else x[i] for i in range(len(x)) ]
    
    a=[11 if x[i]=="A" else x[i] for i in range(len(x)) ] 
    
          
    h=[1 if y[i]=="A" else y[i] for i in range(len(y))]
    
    b=[11 if y[i]=="A" else y[i] for i in range(len(y)) ]
    
    if "A" in x:
       for i in range(len(x)):
           d=d+z[i]
       print(d)
       for i in range(len (x)):
           e=e+a[i]
       print(e)
          
       
    else:
       for i in range(len(x)):
           d=d+z[i]
       print(d)
       
    if "A" in y:
       for i in range(len(y)):
           c=c+h[i]
       print(c)
       for i in range(len(y)):
           f=f+b[i]
       print(f)
      
    else:
       for i in range(len(y)):
           c=c+h[i]
       print(c)
       
    return d,e,c,f
    
  
     
        
def check(d,c):
    
    print(d,c)
    if d<21 and c<21:
        if 21-d<21-c:
            print("Congrats! You have bet the dealer")
            return 2
        elif d==c:
            print("Tap! No one has won")
            return 0
        else:
            print("Sad! Dealer has won!")
            return 1
    elif d>21 and c<=21:
        print("You got busted!! Sad! Dealer has won!")
        return 1
    elif d<=21 and c>21:
        print("Congrats! You have bet the dealer cause the dealer got busted!")
        return 2
    elif d>21 and c>21:
        print("Busted! No one has won!!")
        return 0
         
def BlackJack(x):
      a=0
      x=[10 if x[i] in ["K","J","Q"] else x[i] for i in range(len(x))]
            
      for i in range(len(x)):
           if x[i]=="A":
               x[i]=11

      for i in range(len(x)):
          a=a+x[i]
      if a==21:
          return 2
      
    
def Ace_Calculator(d,e,c,f):
    while True:
        if e<=21 and e>0:
            t=e
        else:
            t=d
        
        if f<=21 and f>0:
            l=f
            break
        else:
            l=c
            break
       
      
    return t,l    
           
def seventeen_check(x):
    a=0
    n=0
    p=0
    x=[10 if x[i] in ["K","Q","J"] else x[i] for i in range(len(x)) ]
    b=[1 if x[i]=="A" else x[i] for i in range(len(x))]
    c=[11 if x[i]=="A" else x[i] for i in range(len(x))]
    
    if "A" in x:
        for i in range(len(x)):
            n=n+b[i]
        for i in range(len(x)):
            p=p+c[i]
        if p>21:
            
            if n>=17:
                return 1
            else:
                return 0
                
        else:
           
            if p>=17:
                return 1
            else:
                return 0
    else:
        for i in range(len(x)):
               a=a+x[i]
        if a>=17:
               return 1
        else:
               return 0               
        

print("Welcome to the BlackJack Casino \U0001f60a \U0001f60a \U0001f60a")
print("\nAdvantage of playing at BlackJack Casino is you will never get busted if you split!")

while True:
    balance=int(input("Set balance:"))
    if balance>0:
        break
    else:
        print("Balance should be greater than zero")


while True:
    s=0
    r=0
    while True:
          try:
            bet=int(input("How much you want to bet?"))
            
          except:
            print("Please enter a string")
          else:
            if bet>balance:
             print("You cannot bet greater than your balance")
            else:
              break
    Record=record(bet,balance)
    loaf=bet
    Record.__betplaced__()
    print(Record)



    print("\n****** Dealer distributes the cards ******* \n")
    x,y=randomgenerator()
    playercard=Player_hand(x)
    dealercard=Dealers_hand(y)
    print("\n",playercard,"\n",dealercard)
    
    
    if y[0]==10 or y[0]=="A":
        n=BlackJack(dealercard.dealers_card)
        if n==2:
            print("Sad! Dealer Got a Black Jack!")
            b=1.5*bet
            print(Record)
            r=1
       
    if r==0: 
        n=BlackJack(playercard.player_card)
        
        if n==2:
            print("Congrats! You are lucky! Got a Black Jack!")
            b=1.5*bet
            Record.__add__(b)
            print(Record)
            r=1
        
        if r==0:
            while True:
                    t=input("Hit(h) or Stand(s) or Double Down(dd) or Surrender(su) or Split(sp): ")
                    if t.lower()=="h":
                       x,y=randomgenerator()
                       playercard.__hit__(x[0])
                       print("Your new card:",playercard)
                       n=BlackJack(playercard.player_card)
                       if n==2:
                           print("Congrats!You Got a BlackJack! You beat Dealer")
                           s=1.5*loaf
                           Record.__add__(s)
                           print(Record)
                           r=1
                           break
                    if t.lower()=="dd":
                            bet=2*bet
                            x,y=randomgenerator()
                            playercard.__hit__(x[0])
                            print("Your new card is:",playercard)
                            n=BlackJack(playercard.player_card)
                            if n==2:
                               print("Congrats!You Got a BlackJack! You beat Dealer")
                               s=1.5*bet
                               Record.__add__(s)
                               print(Record)
                               r=1
                               break
                            break
                    if t.lower()=="su":
                        s=0.5*bet
                        Record.__add__(s)
                        print("You choose to surrender so, ",Record)
                        r=1
                        break
                    if  t.lower()=="sp":
                        s=1
                        a=0
                        b=0
                        print(x)
                        bet=bet*2
                        playercard=Player_hand([x[0]])
                        playercard1=Player_hand([x[1]])
                        x,y=randomgenerator()
                        playercard.__hit__(x[0])
                        print("First Hand:",playercard)
                        playercard1.__hit__(x[1])
                        print("Second Hand:",playercard1)
                        while True:
                            
                            p=input("Do you want to hit? To hit first card press y1 for second card press y2:")
                            if p.lower()=="y1":
                               x,y=randomgenerator()
                               playercard.__hit__(x[0])
                            if p.lower()=="y2":
                               x,y=randomgenerator() 
                               playercard1.__hit__(x[1])
                            print("First Hand:",playercard,"Second Hand:",playercard1)
                            if p.lower()=="n":
                               print("First Hand:",playercard,"Second Hand:",playercard1)
                               break
                        
                        
                        split=[10 if playercard.player_card[i] in ["K","Q","J"] else 11 if playercard.player_card[i]=="A" else playercard.player_card[i] for i in range(len(playercard.player_card))]
                        split2=[10 if playercard1.player_card[i] in ["K","Q","J"] else 11 if playercard1.player_card[i]=="A" else playercard1.player_card[i] for i in range(len(playercard1.player_card))]
                        
                        for i in range(len(playercard.player_card)):
                             a=a+split[i]
                        if a>21 and "A" in playercard.player_card:
                             split=[ 1 if split[i]==11 else split[i] for i in range(len(split))]
                             a=0
                             for i in range(len(split)):
                                a=a+split[i]
                        print(a)       
                        for i in range(len(playercard1.player_card)):
                             b=b+split2[i]
                        if b>21 and "A" in playercard1.player_card:
                             split2=[ 1 if split2[i]==11 else split2[i] for i in range(len(split2))]
                             b=0
                             for i in range(len(split)):
                                b=b+split2[i]
                        print(b)     
                       
                        if playercard.player_card[0]=="A" or playercard1.player_card[0]=="A":
                            if a<21 and b<21:
                                if 21-b<21-a:
                                   playercard.player_card=playercard1.player_card
                                   break
                            elif a>21 and b<21:
                                playercard.player_card=playercard1.player_card
                                break
                            elif b==21:
                                playercard.player_card=playercard1.player
                                break
                            else:
                                break
                        else:
                            if 21-b<21-a:
                                playercard.player_card=playercard1.player_card
                                break
                            elif a==21 or b==21:
                                print("Congrats!! You win!! BlackJack!")
                                b=0.5*bet
                                s=1.5*b
                                Record.__add__(s)
                                print(Record)
                                r=1
                                break
                            elif a>21 and b<21:
                                playercard.player_card=playercard1.player_card
                                break
                            else:
                                break
                    
                    else:
                        break
                    
            if r==0:
                    while True:
                        x,y=randomgenerator()
                        d=seventeen_check(dealercard.dealers_card)
                        if d==0:
                            dealercard.__hit__(y[0])
                        else:
                            print(dealercard.__str__(1))
                            break
                    
                    a=BlackJack(dealercard.dealers_card)
                    if a==2:
                       print("After revealing the hole card which is ", y,"\n")
                       print("BlackJack! Sad!! The Dealer wins")
                       print(dealercard.__str__(1))
                       print(Record)
                       r=1
            if r==0:                     
               d,e,c,f=Calculate(playercard.player_card,dealercard.dealers_card)
               if e==0 and f==0:
                   a=check(d,c)
                   if a==2:
                       
                       Record.__add__(bet)
                       print(Record)
                   if a==0:
                       Record.__add__(0)
                       print(Record)
                   if a==1:
                       Record.__add__(-bet)
                       print(Record)
               else:
                       t,l=Ace_Calculator(d,e,c,f)
                       a=check(t,l)
                       if a==2:
                          Record.__add__(bet)
                          print(Record)
                       if a==0:
                          Record.__add__(0)
                          print(Record)
                       if a==1:
                          Record.__add__(-bet)
                          print(Record)
                        
        if Record.balance>=1:
            balance=Record.balance
            print(balance)
            ask=input("Do you want to continue to play the Game?")
            if ask.lower()=="y":
               continue
            else:
                break
        else:
            break
    
      
    





   