from random import shuffle

class Hand():
  def __init__(self):
    self._hand = []
    self._won_cards = []
  
  def __repr__(self):
    return f"{self._hand}"

  def add_card_hand(self,card):
    if card:
      self._hand.append(card)

  def add_card_won(self,card):
    if card:
      self._won_cards.append(card)

  def remove_card(self):
    card = None
    if self.num_cards_hand() > 0:
      card = self._hand.pop()
    return card
  
  def play_card(self,face_up=True):
    # check if cards are left in hand
    if self.num_cards_hand() < 1:
      # if not shuffle and get the won cards
      self._hand = self.get_cards_won()
    # try to get a card
    card = self.remove_card()
    # if card was returned and should be played face up, flip it
    if card and face_up:
      if card.face_down:
        card.flip_card()
    # otherwise return card face down or None if no cards left
    return card
  
  def num_cards_hand(self):
    return len(self._hand)

  def num_cards_won(self):
    return len(self._won_cards)
  
  def show_hand(self):
    # for card in self._hand:
    #   if card.face_down:
    #     card.flip_card();
    return self._hand

  def hide_hand(self):
    for card in self._hand:
      if not card.face_down:
        card.flip_card()
    return self._hand

  def show_cards(self,cards='hand'):
    show_cards = self._hand if cards == 'hand' else self._won_cards
    for card in show_cards:
      if card.face_down:
        card.flip_card()
    print(show_cards)
    for card in show_cards:
      if not card.face_down:
        card.flip_card()
  
  def get_cards_won(self):
    hand = []
    shuffle(self._won_cards)
    hand = self._won_cards
    self._won_cards = []
    return hand


class Player(Hand):
  def __init__(self,name):
    super().__init__()
    self.name = name

  def __repr__(self):
    return f"{self.name}"