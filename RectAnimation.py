import pygame
pygame.init()

screen = pygame.display.set_mode((700, 1400))
color = (0, 255, 255)
line_width = 7
num = 0

i = 1
running = True
while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	if i % 10 >= 0 and i > 40:
		num = int((i/10)/4)
		
		for x in range(num):
			pygame.draw.line(screen, color, (50+(50*x), 100+(100*x)), (650-(50*x), 100+(100*x)), width=line_width)
			pygame.draw.line(screen, color, (50+(50*x), 100+(100*x)), (50+(50*x), 1200-(100*x)), width=line_width)
			pygame.draw.line(screen, color, (650-(50*x), 100+(100*x)), (650-(50*x), 1200-(100*x)), width=line_width)
			pygame.draw.line(screen, color, (50+(50*x), 1200-(100*x)), (650-(50*x), 1200-(100*x)), width=line_width)
		
	i += 1
	pygame.display.flip()

pygame.quit()
