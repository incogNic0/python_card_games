class Table():
  def __init__(self,Game):
    self.game = Game()
    self.players = []
    self.dealer = []
    self.max_players = None
    self.min_players = None
    self.winner = None
  
  def add_player(self, player):
    self.players.append(player)
    return self.player
  
  def remove_player(self, player):
    removed_player = self.players.remove(player)
    if removed_player:
      return removed_player
    return None

  def new_game(self,players):
    for player in players:
      self.players.append(player)
    
