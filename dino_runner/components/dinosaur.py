import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect() # atualiza o x e y (altura e largura do dino)
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
        
    def jump(self):
        self.image = JUMPING

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect() # atualiza o x e y (altura e largura do dino)
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 35
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
