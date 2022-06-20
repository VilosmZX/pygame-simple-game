import pygame 
from type.Types import _GameObject
from utils import Color

class Player(pygame.sprite.Sprite):
  def __init__(self, x: int, y: int, cls: _GameObject, *groups) -> None:
    self.cls = cls 
    self.x = x 
    self.y = y 
    self._layer = 2
    self.image = pygame.Surface((20, 20))
    self.image.fill(Color.RED)
    self.rect = self.image.get_rect()
    self.rect.x = self.x 
    self.rect.y = self.y 
    self.velocity = 1
    self.score = 0
    self.sound = pygame.mixer.Sound(('assets/sounds/pickup.wav'))
    pygame.mixer.Sound.set_volume(self.sound, 0.1)
    super().__init__(*groups)
    
  def update(self, xp_sprite, xp_list):
    self.handle_particle()
    self.handle_movement()
    self.handle_xp(xp_sprite, xp_list)
    
      
  def handle_movement(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      if self.rect.y > 0:
        self.rect.y -= self.velocity
    if keys[pygame.K_s]:
      if self.rect.y + self.image.get_height() < self.cls.height:
        self.rect.y += self.velocity
    if keys[pygame.K_a]:
      if self.rect.x > 0:
        self.rect.x -= self.velocity
    if keys[pygame.K_d]:
      if self.rect.x + self.image.get_width() < self.cls.width:
        self.rect.x += self.velocity
        
  def handle_xp(self, xp_sprite, xp_list):
    col = pygame.sprite.collide_mask(self, xp_sprite)
    if col:
      self.image = pygame.transform.scale(self.image, (self.image.get_width() + 1, self.image.get_height() + 1))
      pygame.mixer.Sound.play(self.sound)
      xp_sprite.kill()
      self.score += 1
      xp_list.remove(xp_sprite)
      
      
class XP(pygame.sprite.Sprite):
  def __init__(self, x, y, cls: _GameObject, *groups):
    self.cls = cls 
    self._layer = 1
    self.x = x 
    self.y = y 
    self.image = pygame.Surface((12, 12))
    self.image.fill(Color.YELLOW)
    self.rect = self.image.get_rect()
    self.rect.x = self.x 
    self.rect.y = self.y 
    self.shiny = False 
    super().__init__(*groups)
    
    
class Particle(pygame.sprite.Sprite):
  def __init__(self, x, y, cls: _GameObject, *groups):
    self.cls = cls 
    self._layer = 1
    self.x = x 
    self.y = y 
    self.image = pygame.Surface((12, 12))
    self.image.fill(Color.YELLOW)
    self.rect = self.image.get_rect()
    self.rect.x = self.x 
    self.rect.y = self.y 
    self.shiny = False 
    super().__init__(*groups)
    
    
  
    

    
  