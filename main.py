import pygame 
import json 
import sys
from utils import Color
from sprites.Sprites import * 
import random 

class Game:
  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    with open('config.json') as f:
      self.config = json.load(f)
    self.width = self.config['screen']['width']
    self.height = self.config['screen']['height']
    self.fps = self.config['screen']['fps']
    self.window = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('IDK')
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font('assets/fonts/Tetris.ttf', 20)
    self.running = True 
    
    
  def new(self):
    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.xp_sprites = pygame.sprite.LayeredUpdates()
    self.player = Player(10, 10, self, self.all_sprites)
    self.xp_list = []
    for _ in range(10):
      self.xp_list.append(XP(random.randint(0, self.width), random.randint(0, self.height), self, self.xp_sprites))
      
    
  def events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
        
  def show_score(self):
    text = self.font.render(f'Score: {self.player.score}', True, Color.WHITE)
    self.window.blit(text, (20, 20))      
  
        
  def limit_fps(self):
    self.clock.tick(self.fps)
  
  def spawn_xp(self):
    if len(self.xp_list) < 10:
      for _ in range(10 - len(self.xp_list)):
        self.xp_list.append(XP(random.randint(0, self.width), random.randint(0, self.height), self, self.xp_sprites))
  
  def update(self):
    self.spawn_xp()
    self.xp_sprites.update()
    for xp in self.xp_list:
      self.player.update(xp, self.xp_list)    
  
  def draw(self):
    self.window.fill(Color.BLACK)
    self.show_score()
    self.all_sprites.draw(self.window)
    self.xp_sprites.draw(self.window)
    
  def debug(self):
    print(len(self.xp_list))
    
  def run(self):
    while self.running:
      self.limit_fps()
      self.events()
      self.update()
      self.draw()
      pygame.display.update()
      self.debug()
      
if __name__ == '__main__':
  game = Game()
  game.new()
  game.run()