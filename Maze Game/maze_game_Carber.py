import pygame, random

pygame.init()

# --- Constants ---
TILE_SIZE = 30
WIDTH = 20 * TILE_SIZE
HEIGHT = 9 * TILE_SIZE
FPS = 60

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (40, 180, 70)
RED = (220, 50, 50)
BLUE = (50, 100, 230)
GRAY = (120, 120, 120)
PURPLE = (120, 40, 250)
ORANGE = (220, 100, 0)

pygame.mixer.music.load("Super_Mario_Bros_-_Overworld_Main_Theme_(mp3.pm).mp3")
end_music = pygame.mixer.Sound("mario_level_complete.mp3")
key_sound = pygame.mixer.Sound("Mario-coin-sound.mp3")
key_sound.set_volume(0.2)
pygame.mixer.music.play(-1) 
# PLAYER CLASS
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("mario.png").convert()  # Replace player.png with your image filename
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize to fit tile
		self.rect = self.image.get_rect(topleft=(x, y))
		self.speed = 3
		

# TODO 1: Draw the player.
# Hint: Use pygame.draw.circle() or self.image.fill().
		
		

	def update(self, walls):
# TODO 2: Get the keys currently being pressed.
# Hint: keys = pygame.key.get_pressed()
		keys = pygame.key.get_pressed()

# TODO 3: Save the player's original x and y positions.
# Hint: old_x, old_y = self.rect.topleft
		old_x, old_y = self.rect.topleft
# TODO 4: Move left/right/up/down.
# Hint: keys[pygame.K_LEFT], K_RIGHT, K_UP, K_DOWN
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
			self.image = pygame.image.load("marioleft.png").convert()
			self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
			self.image = pygame.image.load("mario.png").convert()
			self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
		if keys[pygame.K_UP]:
			self.rect.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.rect.y += self.speed
# TODO 5: Check for wall collisions.
# Hint: pygame.sprite.spritecollide(self, walls, False)
# Restore the old position if a collision occurs.
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.x = old_x
			self.rect.y = old_y


# WALL CLASS -- PROVIDED
class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect(topleft=(x, y))


# START AND END CLASSES
class StartPoint(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		# TODO 6: Create the image and rectangle.
		# The starting tile should be BLUE.
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect(topleft=(x, y))


class EndPoint(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("images.png").convert()  # Replace player.png with your image filename
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize to fit tile
		self.rect = self.image.get_rect(topleft=(x, y))
		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(GRAY)
		self.rect = self.image.get_rect(topleft=(x, y))


	def update(self, walls):
	# Random movement
		old_x, old_y = self.rect.topleft
		if random.randint(0, 20) == 0:
			self.rect.x += random.choice([-TILE_SIZE, TILE_SIZE, 0])
			self.rect.y += random.choice([-TILE_SIZE, TILE_SIZE, 0])
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.x = old_x
			self.rect.y = old_y

class Key(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(PURPLE)
		self.rect = self.image.get_rect(topleft=(x, y))
		
class Speed(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill(ORANGE)
		self.rect = self.image.get_rect(topleft=(x, y))


# LOAD MAZE FROM FILE
def load_maze(maze):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()
	enemy_sprites = pygame.sprite.Group()
	key_sprites = pygame.sprite.Group()
	print("loading Maze")
	player = None
	start_point = None
	end_point = None
	enemy = None
	speed = None


	with open(maze, "r") as file:
		maze_level = [line.strip() for line in file]
		print( maze_level )
	
	row_index = -1
	for  row in maze_level:
		row_index += 1
		for col_index, char in enumerate(row):
			x = col_index * TILE_SIZE
			y =  row_index * TILE_SIZE
	
			if (char == "1"):
				wall = Wall(x, y)
				all_sprites.add(wall)
				wall_sprites.add(wall)
			elif ( char == "S"):
				start_point = StartPoint(x, y)
				player = Player(x, y)
				all_sprites.add(start_point)
				all_sprites.add(player)
			elif (char == "E"):
				end_point = EndPoint(x, y)
				all_sprites.add(end_point)
			elif ( char == "D"):
				enemy = Enemy(x, y)
				all_sprites.add(enemy)
				enemy_sprites.add(enemy)
			elif ( char == "K"):
				key = Key(x, y)
				all_sprites.add(key)
				key_sprites.add(key)
			elif ( char == "Q"):
				speed = Speed(x, y)
				all_sprites.add(speed)
				
				
	# Add each maze object to all_sprites.
	# Add walls to wall_sprites as well.

	# Add the player to all_sprites after building the maze.

	# TODO 13: Return all five values:
	# all_sprites, wall_sprites, player, start_point, end_point
	return all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed


# MAIN GAME
def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Maze Game")
	clock = pygame.time.Clock()
	level = "1"
	keys = 0
	
	# TODO 14: Load the maze.
	# Hint: Call load_maze("maze.txt")
	all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed = load_maze("maze" + level + ".txt")
	running = True
	game_won = False
	
	font = pygame.font.SysFont(None, 50)

	while running:
		# TODO 15: Handle events.
		# Hint: pygame.event.get()
		# Allow the player to close the window.
		enemy_sprites.update(wall_sprites)
		player.update(wall_sprites)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r and game_won:
					player.rect.topleft = start_point.rect.topleft
					game_won = False
			if not game_won:
		# TODO 16: Update the player.
				
		# TODO 17: Check if the player reached the exit
		# Hint: pygame.sprite.collide_rect()
				
				if  pygame.sprite.collide_rect(player, end_point) and level == "1":
					screen.blit
					level = "2"
					all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed = load_maze("maze" + level + ".txt")
					print("level 2")
					player.speed = 3
				elif keys == 2 and pygame.sprite.collide_rect(player, end_point) and level == "2":
					screen.blit
					level = "3"
					print(level)
					all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed = load_maze("maze" + level + ".txt")
					print("Level 3")
		if pygame.sprite.spritecollide(player, enemy_sprites, False):
			all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed = load_maze("maze" + level + ".txt")
			if level == "2":
				keys = 0
			elif level == "3":
				keys = 2
		if pygame.sprite.spritecollide(player, key_sprites, True):
			keys += 1
			key_sound.play()
			print(keys)
		if pygame.sprite.collide_rect(player, speed):
			player.speed = 1
				
		
		# TODO 18: Fill the background and draw all sprites.
		screen.fill(WHITE)
		all_sprites.draw(screen)
		# TODO 19: If game_won is True, display "You Win!"
		if (level == "3"):
			if keys == 6 and pygame.sprite.collide_rect(player, end_point):
				print("You Win!")
				pygame.mixer.music.stop()
				end_music.play()
				game_won = True
			
				if __name__ == "__main__":
					main()
		if game_won == True:
			text = font.render("You Win!", True, GREEN)
			text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

			# Dark background behind the message.
			background = text_rect.inflate(30, 20)
			pygame.draw.rect(screen, BLACK, background)
			screen.blit(text, text_rect)

			restart_font = pygame.font.SysFont(None, 24)
			restart_text = restart_font.render("Press R to play again", True, GREEN)
			restart_rect = restart_text.get_rect(
				center=(WIDTH // 2, HEIGHT // 2 + 40)
			)
			screen.blit(restart_text, restart_rect)
			
			restart = input("Play Again?")
			
			if restart == "R" or restart == "r":
				level = "1"
				keys = 0
				all_sprites, wall_sprites, player, start_point, end_point, enemy_sprites, key_sprites, speed = load_maze("maze" + level + ".txt")
				game_won = False
			
				

		#screen.blit(restart_text, restart_rect)
		 
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()


if __name__ == "__main__":
	main()
