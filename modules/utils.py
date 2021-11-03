def is_valid_input(input, valid_responses):
  try:
    valid_responses.index(input)
    return True
  except ValueError:
    return False

def is_game_over(players):
  for player in players:
    if player.get_num_cards() == 0:
      return True
  return False