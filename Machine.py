import pygame

with open("File.lx", "rb") as f: mem = f.read()

pygame.init()

display = pygame.display.set_mode((16, len(mem)))

running = True

while running:
	running = not(pygame.QUIT in [event.type for event in pygame.event.get()])