from random import shuffle

class Card():
    def __init__(self,value,suit=''):
        self.value = value
        self.suit = suit
        self.face_down = True
    
    def __repr__(self):
      if not self.face_down:
        return f"{self.value}{self.suit}"
      else:
        return '*'
    
    def flip_card(self):
      if self.face_down:
        self.face_down = False
      else:
        self.face_down = True

class Deck():
    
    def __init__(self,values,suits):
        self._cards = [Card(value,suit) for suit in suits for value in values]
        self._full_deck = self.count()
    
    def __repr__(self):
        return ','.join([card.value + card.suit for card in self._cards])
    
    def count(self):
        return len(self._cards)
    
    def shuffle(self):
        if self.count() != self._full_deck:
            raise ValueError(f"Only a full deck of {self._full_deck} can be shuffled. {self.count()} currently in deck.")
        return shuffle(self._cards)
    
    def deal_card(self):
      return self._cards.pop(0)

    def deal(self,desired_cards=1):
        actual_cards = min(desired_cards,len(self._cards))
        dealt_cards = self._cards[-actual_cards:]
        self._cards = self._cards[:-actual_cards]
        return dealt_cards
    
    def deal_start(self, func):
      #run specified game's function for starting deal
      return func()

class Standard(Deck):
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # Order:  Spades, Diamonds, Clubs, Hearts
    suits = ['\u2660','\u2666','\u2665','\u2663']
    
    def __init__(self,jokers=False):
        super().__init__(Standard.values,Standard.suits)
        #Jokers not included by default.
        if jokers==True:
            self._include_jokers()
            self._full_deck = self.count()
    
    def _include_jokers(self):
        #'Big Joker' denoted by all caps, 'Little Joker' is lowercase
        jokers = [Card('JOKER'),Card('joker')]
        self._cards = jokers + self._cards

class Pinnacle(Deck):
    values = ['9','10','J','Q','K','A']
    # Order:  Spades, Diamonds, Clubs, Hearts
    suits = ['\u2660','\u2666','\u2665','\u2663']

    def __init__(self):
        super().__init__(Pinnacle.values, Pinnacle.suits)
        self._cards = self._cards * 2
        self._full_deck = 48


