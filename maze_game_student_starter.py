import pygame

pygame.init()

#=======================================================================
#                            CONSTANTS
#=======================================================================

TILE_SIZE = 34
WIDTH = 29 * TILE_SIZE
HEIGHT = 17 * TILE_SIZE
FPS = 60
font = pygame.font.SysFont(None, 48)

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

#=======================================================================
#                       	   COLORS
#=======================================================================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
ORANGE = (252, 149, 88)
GOLD = (255, 210, 40)
GREEN = (111, 194, 118)
DARK_GREEN = (20, 100, 40)
BLUE = (50, 100, 230)
PURPLE = (184, 147, 217)

#=======================================================================
#                          PLAYER CLASS
#=======================================================================
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("images.jpg").convert_alpha()
		self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
		self.rect = self.image.get_rect(topleft = (x, y))

		self.speed = 2

	def update(self, walls):
		# Save the old position so we can undo
		# movement if the player hits a wall.
		old_x, old_y = self.rect.topleft

		keys = pygame.key.get_pressed()

		# Move horizontally
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed

		# Undo horizontal movement if blocked
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.x = old_x

		# Move vertically
		if keys[pygame.K_UP]:
			self.rect.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.rect.y += self.speed

		# Undo vertical movement if blocked
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.y = old_y

#=======================================================================
#                            WALL CLASS
#=======================================================================

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                        DANGER ZONE CLASS
#=======================================================================

class DangerZone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                              KEY CLASS
#=======================================================================

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                          ROADBLOCK CLASS
#=======================================================================

class Roadblock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                      START AND END CLASSES
#=======================================================================

class StartPoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface(
            (TILE_SIZE, TILE_SIZE)
        )
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect(topleft=(x, y))

class EndPoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface(
            (TILE_SIZE, TILE_SIZE)
        )
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

#=======================================================================
#                   LOADING THE MAZE - LVL 1
#=======================================================================

def load_maze_LVL1(filename):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()

	player = None
	start_point = None
	end_point = None

	with open (filename, "r") as file:
		maze_level = [line.strip() for line in file]

	for row_index, row in enumerate (maze_level):
			for col_index, char in enumerate (row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				if char == "1":
					wall = Wall(x,y)
					all_sprites.add(wall)
					wall_sprites.add(wall)
				elif char == "S":
					start_point = StartPoint (x,y)
					player = Player (x,y)
					all_sprites.add (start_point)
					all_sprites.add(player)
				elif char =="D":
					danger_zone = DangerZone (x,y)
					all_sprites.add(danger_zone)
				elif char =="K":
					key = Key (x,y)
					all_sprites.add(key)
				elif char =="R":
					roadblock = Roadblock (x,y)
					all_sprites.add(roadblock)
				elif char =="E":
					end_point = EndPoint (x,y)
					all_sprites.add(end_point)


	return all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point
	pass
	
#=======================================================================
#                    LOADING THE MAZE - LVL 2
#=======================================================================
	
def load_maze_LVL2(filename):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()

	player = None
	start_point = None
	end_point = None

	with open (filename, "r") as file:
		maze_level = [line.strip() for line in file]

	for row_index, row in enumerate (maze_level):
			for col_index, char in enumerate (row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				if char == "1":
					wall = Wall(x,y)
					all_sprites.add(wall)
					wall_sprites.add(wall)
				elif char == "S":
					start_point = StartPoint (x,y)
					player = Player (x,y)
					all_sprites.add (start_point)
					all_sprites.add(player)
				elif char =="D":
					danger_zone = DangerZone (x,y)
					all_sprites.add(danger_zone)
				elif char =="K":
					key = Key (x,y)
					all_sprites.add(key)
				elif char =="R":
					roadblock = Roadblock (x,y)
					all_sprites.add(roadblock)
				elif char =="E":
					end_point = EndPoint (x,y)
					all_sprites.add(end_point)

	return all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point
	pass
	
	
#=======================================================================
#                    LOADING THE MAZE - LVL 3
#=======================================================================
	
def load_maze_LVL3(filename):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()

	player = None
	start_point = None
	end_point = None

	with open (filename, "r") as file:
		maze_level = [line.strip() for line in file]

	for row_index, row in enumerate (maze_level):
			for col_index, char in enumerate (row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				if char == "1":
					wall = Wall(x,y)
					all_sprites.add(wall)
					wall_sprites.add(wall)
				elif char == "S":
					start_point = StartPoint (x,y)
					player = Player (x,y)
					all_sprites.add (start_point)
					all_sprites.add(player)
				elif char =="D":
					danger_zone = DangerZone (x,y)
					all_sprites.add(danger_zone)
				elif char =="K":
					key = Key (x,y)
					all_sprites.add(key)
				elif char =="R":
					roadblock = Roadblock (x,y)
					all_sprites.add(roadblock)
				elif char =="E":
					end_point = EndPoint (x,y)
					all_sprites.add(end_point)

	return all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point
	pass
	
#=======================================================================
#                             MAIN GAME
#=======================================================================

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Maze Game")
	
	clock = pygame.time.Clock()

	all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point = load_maze_LVL1("LVL1.txt")

	running = True
	game_won = False
	lives = 3

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r and game_won:
					player.rest.topleft = start_point.rect.topleft
					game_won = False
					
			if pygame.sprite.collide_rect(player, key):
				game_won = True
				
			if pygame.sprite.collide_rect(player, danger_zone): #If player collides into the danger zone, remove a life
				lives -= 1
				print(lives)
				if lives < 1:
					print("Out of lives")
					screen.fill(WHITE)
					text = font.render("You're Out of Lives!", False, RED) 
					text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
					
					background = text_rect.inflate(30, 20)
					pygame.draw.rect(screen, BLACK, background)
					screen.blit(text, text_rect)
			
			if pygame.sprite.collide_rect(player, roadblock):
				player.speed = 9
						
		if not game_won:
			player.update(wall_sprites)
			
			if pygame.sprite.collide_rect(player, end_point):
					game_won = True

		screen.fill(WHITE)
		all_sprites.draw(screen)

		if game_won:
			text = font.render("NEXT LEVEL - LEVEL 2", True, GOLD) 
			text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
			
			background = text_rect.inflate(30, 20)
			pygame.draw.rect(screen, BLACK, background)
			screen.blit(text, text_rect)
			
			all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point = load_maze_LVL2("LVL2.txt")
			
			running = True
			game_won = False
		
			while running:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r and game_won:
							player.rest.topleft = start_point.rect.topleft
							game_won = False
							
					if pygame.sprite.collide_rect(player, key):
						game_won = True
					
					if pygame.sprite.collide_rect(player, roadblock):
						player.speed = 9
						
					if pygame.sprite.collide_rect(player, danger_zone): #If player collides into the danger zone, remove a life
						lives -= 1
						print(lives)
						if lives < 1:
							print("Out of lives")
							screen.fill(WHITE)
							text = font.render("You're Out of Lives!", False, RED) 
							text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
							
							background = text_rect.inflate(30, 20)
							pygame.draw.rect(screen, BLACK, background)
							screen.blit(text, text_rect)
								
				if not game_won:
					player.update(wall_sprites)
					if pygame.sprite.collide_rect(player, end_point):
						game_won = True

				screen.fill(WHITE)
				all_sprites.draw(screen)

				if game_won:
					text = font.render("NEXT LEVEL - LEVEL 3", True, GOLD) 
					text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
					
					background = text_rect.inflate(30, 20)
					pygame.draw.rect(screen, BLACK, background)
					screen.blit(text, text_rect)
					
					all_sprites, wall_sprites, player, start_point, danger_zone, key, roadblock, end_point = load_maze_LVL2("LVL3.txt")
					
					running = True
					game_won = False
				
					while running:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = False
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_r and game_won:
									player.rest.topleft = start_point.rect.topleft
									game_won = False
									
							if pygame.sprite.collide_rect(player, key):
								game_won = True
								
							if pygame.sprite.collide_rect(player, danger_zone): #If player collides into the danger zone, remove a life
								lives -= 1
								print(lives)
								if lives < 1:
									print("Out of lives")
									screen.fill(WHITE)
									text = font.render("You're Out of Lives!", False, RED) 
									text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
										
									background = text_rect.inflate(120, 90)
									pygame.draw.rect(screen, BLACK, background)
									screen.blit(text, text_rect)
							
							if pygame.sprite.collide_rect(player, roadblock):
								player.speed = 9
										
						if not game_won:
							player.update(wall_sprites)

							if pygame.sprite.collide_rect(player, end_point):
									game_won = True

						screen.fill(WHITE)
						all_sprites.draw(screen)

						if game_won:
							text = font.render("You Win!", True, GOLD) 
							text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2))
							
							background = text_rect.inflate(120, 90)
							pygame.draw.rect(screen, BLACK, background)
							screen.blit(text, text_rect)
							
							restart_font = pygame.font.SysFont(None, 24)
							restart_text = restart_font.render("Restart to play again!", True, WHITE)
							restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
							screen.blit(restart_text, restart_rect)
					
						pygame.display.flip()
						clock.tick(FPS)
			
				pygame.display.flip()
				clock.tick(FPS)
	
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()

if __name__ == "__main__":
	main()
