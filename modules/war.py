from modules.player import *
from modules.deck import Card, Standard
from modules.utils import is_valid_input

class War(Standard):
  def __init__(self,players):
    super().__init__()
    self.players = players
    self.starting_cards = 52
    self.winner = None

  def deal_starting_hands(self):
    cards_to_deal = self.deal(self.starting_cards)
    while cards_to_deal:
      for player in self.players:
        if cards_to_deal:
          player.add_card_hand(cards_to_deal.pop())

  def new_game(self,players):
    for player in players:
      self.add_player(player)
    self.deal_start()
    
  def get_rank_value(self,card):
    face_cards = { 'J': 11, 'Q':12, 'K':13, 'A':14 }
    output = 0
    if not card or card.face_down:
      return output
    try:
      output = int(card.value)
    except ValueError:
      output = face_cards[card.value]
    finally:
      return output

  def get_hand_winner(self,played_cards):
    highest_rank = 0
    winner = None
    for player in played_cards:
      # get value of last card played
      cards = played_cards[player]
      last_card = len(cards) -1
      card_rank = self.get_rank_value(cards[last_card])
      if card_rank == highest_rank:
        winner = None # Draw equals war
      if card_rank > highest_rank:
        highest_rank = card_rank
        winner = player
    return winner
  
  def game_over(self):
    for player in self.players:
      if player.num_cards_hand() < 1 and player.num_cards_won() < 1:
        return True
    return False
  
  def print_hand_result(self,players_cards, winner):
    print('\n------------------------')
    print(f'Hand results:')
    print('------------------------')
    for player in players_cards:
      cards = players_cards[player]
      last_index = len(cards) - 1
      if last_index > 0:
        # if hand resulted in war display last two cards played else display last
        print(f'{player} played: {cards[last_index-1]} {cards[last_index]}')
      else:
        print(f'{player} played: {cards[last_index]}')
    print('------------------------')
    if winner:
      print(f'{winner} won the hand')
    else:
      print('War!')
      return

  def print_cards_remaining(self):
    print('------------------------')
    print('Total Cards:')
    for player in self.players:
      print(f'{player}: {player.num_cards_hand() + player.num_cards_won()} card(s)')
    print('------------------------\n')

  def print_game_result(self):
    if self.winner == 'default':
      print('Game Over :(')
    else:
      print(f'{self.winner} won the game!\n'.upper())

  def deal_war(self, played_cards):
    for player in played_cards:
      card_face_down = player.play_card(face_up=False)
      card_face_up = player.play_card()
      played_cards[player].extend([card_face_down, card_face_up])
    return played_cards
  
  def collect_cards(self, played_cards, winner):
    all_cards = []
    for player in played_cards:
      all_cards.extend(played_cards[player])
    for card in all_cards:
      if card:
        if not card.face_down:
          card.flip_card()
        winner.add_card_won(card)

  def play_hand(self):
    played_cards = {}
    hand_winner = None
    for player in self.players:
      player.show_cards('hand')
      player.show_cards('won')
      card = player.play_card()
      played_cards[player] = [card]
    while not hand_winner:
      hand_winner = self.get_hand_winner(played_cards)
      self.print_hand_result(played_cards, hand_winner)
      if hand_winner:
        self.collect_cards(played_cards, hand_winner)
      else:
        while True:
          player_input = input('Press [enter] to continue:')
          if is_valid_input(player_input, ''):
            played_cards = self.deal_war(played_cards)
            break     
      continue
    self.print_cards_remaining()
    return hand_winner

