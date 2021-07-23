try:
	import pygame, os, platform, random,math
	from pygame.locals import *
except ImportError:
	print("Erreur d'importation des modules supplémentaires...")
else:
	pygame.init()
	clock = pygame.time.Clock()
	WHITE,BLACK = (255,255,255),(0,0,0)
	dimensions = (800,800)
	screen = (pygame.display.Info().current_w,pygame.display.Info().current_h)
	positions = ((screen[0]-dimensions[0])//2, (screen[1]-dimensions[1])//2)
	os.environ["SDL_VIDEO_WINDOW_POS"] = f"{positions[0]},{positions[1]}"
	video = pygame.display.set_mode(dimensions, pygame.HWACCEL | pygame.HWSURFACE)
	pygame.display.set_caption("Spirale d'Ulam")
	video.fill(WHITE)
	pygame.display.update()

	def sqrtHeron(number,iterations=10**3):
		result = 1
		for k in range(iterations):
			result = (result + number/result)/2
		if result.is_integer():
			return int(result)
		return result

	def isPrime(number):
		sqrt, i = int(sqrtHeron(number)),0
		for k in range(2, sqrt+1):
			if number % k == 0:
				i += 1
		if i == 0:
			return True
		return False

	def changeDirection(direction):
		if direction == "right":return "bottom"
		elif direction == "bottom":return "left"
		elif direction == "left":return "up"
		elif direction == "up":return "right"
		else:raise ValueError("You must enter a direction")

	def changePosition(direction,x,y):
		if direction == "bottom":return x,y+1
		elif direction == "left":return x-1,y
		elif direction == "right":return x+1,y
		elif direction == "up":return x,y-1
		else:return 0,0

	def display(table):
		maxString, result = 0, ""
		for k in range(len(table)):
			for c in range(len(table[k])):
				tmp = len(str(table[k][c]))
				if maxString < tmp:
					maxString = tmp
		for k in range(len(table)):
			for c in range(len(table[k])):
				result += f"{'0'*(maxString-len(str(table[k][c])))}{table[k][c]} "
			print(result)
			result = ""

	def spiralUlam(ordre=5):
		number,x,y,spiral = ordre**2,0,0,[]
		for k in range(ordre):
			spiral.append([])
			for c in range(ordre):
				spiral[k].append(0)
		for k in range(ordre):
			spiral[y][x] = number
			x += 1
			number -= 1
		x, direction, turn, number1 = ordre-1, "bottom", 0, ordre-1
		for k in range(ordre**2-ordre):
			for c in range(number1):
				x,y = changePosition(direction,x,y)
				spiral[y][x] = number
				number -= 1
			direction = changeDirection(direction)
			turn += 1
			if turn % 2 == 0:
				turn = 0
				number1 -= 1
		return spiral

	spiral = spiralUlam(160)
	dx,dy = 5,5
	x,y = 0,0

	for k in range(len(spiral)):
		for c in range(len(spiral[k])):
			if isPrime(spiral[k][c]):
				pygame.draw.rect(video, BLACK, pygame.Rect(x,y,dx,dy))
			x+=5
		y += 5
		x = 0
		pygame.display.update()


	started = True
	while started:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				started = False
	pygame.init()

