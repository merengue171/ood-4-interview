"""
BlackJack Game:
- Dealer and player
- target 21
- cases: Ace: 1 or 11
- Face Cards > 10 = 10

Design the game Blackjack:
For a given deck of cards, there are two ppl playing. Dealer and player. The dealer takes two cards and one of them is hidden. The player
get two cards after that he can choose to hit or stand. Get one more card or give dealer the move. The dealer makes a move if his total value
of card is less than 17.
The first person to reach 21 wins. All face cards are worth 10 except for ACE which can be 1 or 11 depending on the situation

Requirements:
- to evaluate player score
- 52 cards, 4 face cards
- Dealer will distribute cards
- Dealer and 1 player

Entites:
    Dealer, Player, Deck, Card, Hand
Singleton:
    Game
"""
from abc import ABC, abstractmethod
from enum import Enum

class Suit(Enum):
    Spade, Diamond, Heart, Flower = 1, 2, 3, 4
# class Value(Enum):
#     Ace, Two, Three
    
class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
    
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        return self.value
    
    def getActualValue(self):
        if self.value > 10:
            return 10
        return self.value

class Deck:
    def __init__(self) -> None:
        self.list_of_cards = []
        self.__create_deck()
        self.__shuffle()
        
    def __create_deck(self):
        for suit in Suit:
            for j in range(1, 14):
                self.list_of_cards.append(Card(suit, j))
    
    def __shuffle(self):
        pass
    
    def remove_card(self):
        if len(self.list_of_cards) < 1:
            raise ValueError("No cards")
        return self.list_of_cards.pop(0)

class Person(ABC):
    def __init__(self, id):
        self.id = id
        self.cards = []
        self.countAces = 0
    
    def getScore(self):
        score = 0
        for card in self.cards:
            if card.getActualValue() != 1:
                score += card.getActualValue()
            if score > 21:
                return score
        
        for i in range(self.countAces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
                
        return score
    
    def addCard(self, card):
        if card.getActualValue() == 1:
            self.countAces += 1
        self.cards.append(card)
    
    @abstractmethod
    def canPlay(self):
        pass
    
    @abstractmethod
    def wantToPlay(self):
        pass

class Dealer(Person):
    def __init__(self, id):
        super().__init__(id)
    
    def canPlay(self):
        return self.getScore() < 21
    def wantToPlay(self):
        return self.getScore() < 17

class Player(Person):
    def __init__(self, id):
        super().__init__(id)
    
    def canPlay(self):
        return self.getScore() < 21
    def wantToPlay(self):
        return self.getScore() < 17 # can be elaborated

class Game():
    def __init__(self) -> None:
        self.deck = Deck()
        self.dealer = Dealer(0)
        self.player = Player(1)
    
    def play(self):
        for i in range(2):
            self.dealer.addCard(self.deck.remove_card())
        for i in range(2):
            self.player.addCard(self.deck.remove_card())

        # while True:
        #   play
        #
        # getWinner
        
        while True:
            if self.getWinner() in [self.dealer, self.player]:
                return self.getWinner() 
            if self.dealer.wantToPlay():
                self.dealer.addCard(self.deck.remove_card())
            if self.player.wantToPlay():
                self.player.addCard(self.deck.remove_card())
            
        
    def getWinner(self):
        pass