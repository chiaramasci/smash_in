import pygame
from gpiozero import Button

# path where the sound is located
SOUND_PATH = "/home/pi/Desktop/smash_in_proto/smash_in/sounds/sound.wav"

# buttons setting
btn_1 = Button(2)
btn_2 = Button(3)
btn_3 = Button(4)
btn_4 = Button(17)
btn_5 = Button(27)
btn_6 = Button(22)

# sound initialization
pygame.init()
sound = pygame.mixer.Sound(SOUND_PATH)

sound.play

def printt():
	print("banana	")

# action
while True:
	btn_1.when_pressed = sound.play
	btn_2.when_pressed = sound.play
	btn_3.when_pressed = sound.play
	btn_4.when_pressed = sound.play
	btn_5.when_pressed = sound.play
	btn_6.when_pressed = sound.play
