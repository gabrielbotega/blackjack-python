# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:05:36 2022

@author: Gabriel Botega
"""

#import the dealer from Classes
from Classes import Dealer
from Classes import Player
from Func import summing

#Dealer created
dealer = Dealer()

#dealer must shuffle the deck
dealer.shuffle()

#Player arrives
wannaplay = input("Hello friend, wanna play? (Y/N)").lower()
if wannaplay == "y":
        
    #need to create the player
    name = input("What's your name then?  ")

    #taking balance - this while loop guarantees that the player will insert a number
    while True:
        try:
            balance = int(input("How much do you have to play?  "))
        except:
            print("Sorry, did'nt understand")
            continue
        else:
            break
    #creates the player one instance    
    player_one = Player(name, balance)
    
    ###### letsgo declaration allows us to have several games with the same player
    letsgo = True

    # while the player is willing to play, this happens
    while letsgo:
        print(f"Your balance is {player_one.balance}.") #printing balance
        
        while True: #this block assures the "Y/N" to continue
            continuing = input("Want to continue the game? (Y/N) ").upper() #want to continue to play (change the letsgo variable)
            if (continuing == "N" or continuing == "Y"):
                break
            else:
                continue

        #If the player does not want to play, break
        if continuing == "N":
            letsgo = False
            break
        else:           
            #need to bet an integer
            while True:
                try:
                    bet = int(input("How much do you want to bet?  "))
                except:
                    print("Sorry, did'nt understand")
                    continue
                else:
                    print(f"\nOK. I will cover. There are USD {bet*2} on the table.\n")
                    break

            #table money should be easier to deal with
            player_one.pay_bet(bet)
            dealer.pay_bet(bet)
            table_money = bet*2
            
            #Dealer needs to deal the cards
            #dealing to player
            player_cards =[]
            dealer_cards =[]
            player_cards_value =[]
            dealer_cards_value =[]
            for i in range(2):
                player_cards.append(dealer.deal_card()) #suit and rank
                dealer_cards.append(dealer.deal_card()) #suit and rank
                player_cards_value.append(player_cards[i].value) #value
                dealer_cards_value.append(dealer_cards[i].value) #value
                
            print(f"\n{name}, your cards are: {player_cards[0]} and {player_cards[1]}.")
            print(f"\nMy card is: {dealer_cards[0]}\n")
            
            #there is the possibility of getting 2 aces. thus:
            if summing(player_cards_value) > 21:
                player_cards_value[-1] = 1
                
            print(f"\n{name}, you have {summing(player_cards_value)} points.\n")
            
            #game_on as a method to keep playing 
            game_on = True
            while game_on:
                #knowing what you have, player must decide if want to hit or stay
                decision = "a"
                while decision not in ["H", "S"]:
                    decision = input("Hit or Stay? (H/S) ").upper()
                
                '''
                IF HIT BLOCK ###################
                '''
                counthit = 2 #start with two cards already
                while decision == "H":
                    player_cards.append(dealer.deal_card())
                    player_cards_value.append(player_cards[counthit].value)
                    for i in range(counthit+1):
                        print(f"{name}'s {i+1} card:  {player_cards[i]}")
                   
                    #need to verify the summing and Ace
                    if summing(player_cards_value) > 21:
                        if player_cards_value[-1] == 11:
                            player_cards_value[-1] = 1
                        else:
                            print(f"\n{name}, you have {summing(player_cards_value)} points.\n")
                            print("You've lost.")
                            game_on = False
                            dealer.colect_money(table_money) #dealer collecting the bet
                            break
                    else:
                        print(f"\n{name}, you have {summing(player_cards_value)} points.\n")
                        decision = "a"
                        # while decision not in ["H", "S"]:
                        #     decision = input("Hit or Stay? (H/S) ")
                        counthit +=1   
                    
                    print(f"\n{name}, you have {summing(player_cards_value)} points.\n")
        
                '''
                END OF IF HIT BLOCK ###############
                '''
        
                '''
                STARTING THE STAY BLOCK. HERE, THE DEALER WILL DO ALL THE ACTION AND DECISION
                '''
                if decision == "S":
                    #must show the card that is still unknown
                    print(f"\nSo, my first card was {dealer_cards[0]}. Now, turning the second: {dealer_cards[1]}.\n")
                    print(f"\nMy sum is: {summing(dealer_cards_value)}.")
                    
                    ########## Dealer hit untill win or burst ##############
                    dealer_win = True
                    count_dealer = 1 #already has 1 cards
                    while dealer_win:
                        if summing(dealer_cards_value) > 21:
                            if dealer_cards_value[-1] == 11:
                                dealer_cards_value[-1] = 1
                            else:
                                print(f"\nWell, I have {summing(dealer_cards_value)} points.\n")
                                print("\nI've lost.\n")
                                dealer_win = False
                                game_on = False
                                player_one.colect_money(table_money) #player collecting the bet
                                break
                        #Verify if dealer won
                        elif summing(dealer_cards_value) > summing(player_cards_value):
                            for i in range(counthit):
                                print(f"{name}'s {i+1} card:  {player_cards[i]}")
                            print("\n")
                            for i in range(count_dealer+1):
                                print(f"Dealer's {i+1} card:  {dealer_cards[i]}")
                            print(f"\n I've made {summing(dealer_cards_value)}.\n You've made {summing(player_cards_value)}.\n")
                            print("I've won!\n")
                            dealer_win = False
                            game_on = False
                            dealer.colect_money(table_money) #dealer collecting the bet
                            break
                        
                        else:
                            count_dealer +=1
                            print("\nHIT!\n")
                            dealer_cards.append(dealer.deal_card())
                            dealer_cards_value.append(dealer_cards[count_dealer].value)
                            for i in range(count_dealer+1):
                                print(f"Dealer's {i+1} card:  {dealer_cards[i]}")
                            print(f"\n I have {summing(dealer_cards_value)} points.\n")
                
                '''
                END OF STAY BLOCK
                '''
    

else:
    print("OK, maybe later. See you")        