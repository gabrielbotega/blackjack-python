# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:32:07 2022

@author: Gabriel Botega
"""


'''
random module will be used to shuffle the deck. Therefore using random.suffle()
'''
import random #gonna be used to shuffle the deck

'''
To create the deck I need to have some card's aspect, such as Suit & Rank. To make it easier to sum,
transforming the rank to value is a good solution
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

'''
The game is based in comparing cards. Therefore it'll be useful having a Card class and a 
Dealer class, which i can operate
'''

class Card:
    '''
    Card has two parameters: suit and rank. It also must have its value
    '''
    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Dealer:
    '''
    As a Dealer attribute, it must have its cards
    '''
    def __init__(self, balance = 1000000): #the house has all the money
        self.all_cards = []
        self.balance = balance
        for suit in suits:
            for rank in ranks:
                created_cards = Card(suit,rank)
                self.all_cards.append(created_cards)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_card(self):
        return self.all_cards.pop()
    
    def colect_money(self,table_money):
        self.balance += table_money
        
    def pay_bet(self, player_bet):
        if player_bet > self.balance:
            print("Do not have funds")
        else:
            self.balance -= player_bet
            
            
'''
must create the player here
'''

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def colect_money(self, table_money):
        self.balance += table_money
        
    def pay_bet(self, bet):
        self.balance -= bet
        
    def __str__(self):
        return f'My name is  {self.name}'