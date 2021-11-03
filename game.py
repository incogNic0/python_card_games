from modules.deck import *
from modules.player import *
from modules.war import *
from modules.utils import *


def play_game():
  players = [Player('You'), Player('Computer')]
  game = War(players)
  game.shuffle()
  game.deal_start(game.deal_starting_hands)
  while not game.winner:
    player_decision = input('Press [enter] to play turn or [q] to quit: ')
    if is_valid_input(player_decision, ['','q']):
      if player_decision == '':
        hand_winner = game.play_hand()
        if game.game_over():
          game.winner = hand_winner
      elif player_decision.lower() == 'q':
        game.winner = 'default'
    else:
      print('Please enter a valid option.')
  game.print_game_result()
  return


def start_game():
  quit_game = False
  while not quit_game:
    player_input = input('Start new game? (y/n): ').lower()
    if is_valid_input(player_input,['y','n']):
      if player_input == 'y':
        print('\nShuffling and dealing cards....\n')
        play_game()
        continue
      else:
        print('Goodbye!')
        quit_game = True
    else:
      print("Please enter 'y' or 'n' only")
      continue
start_game()

