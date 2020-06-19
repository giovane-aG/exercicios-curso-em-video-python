import pygame
from pygame import mixer

mixer.init()
pygame.init()
mixer.music.load('rider.mp3')
mixer.music.play()
pygame.event.wait()
