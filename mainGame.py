import pygame, random

pygame.init()

#=======================================================================
#                            CONSTANTS
#=======================================================================

TILE_SIZE = 20
WIDTH = 50 * TILE_SIZE
HEIGHT = 30 * TILE_SIZE
FPS = 60
font = pygame.font.SysFont(None, 48)

PLAYER_WIDTH = 15
PLAYER_HEIGHT = 15

#=======================================================================
#                       	     COLORS
#=======================================================================

WHITE      = (255, 255, 255)
LIGHT_BLUE = (204, 229, 255)
BLUE       = (102, 178, 255)
TURQUOISE  = (153, 255, 255)
NAVY_BLUE  = (0, 0, 128)
BLACK      = (0, 0, 0)

GOLD = (255, 210, 40)
SAND = (227, 194, 138)
LIGHT_GRAY = (176, 169, 158)
GREEN = (43, 84, 53)
CORAL = (214, 120, 155)

#=======================================================================
#                          PLAYER CLASS
#=======================================================================
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("fish.jpg")
		self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize to fit tile
		self.rect = self.image.get_rect(topleft=(x, y))
		
		self.speed = 5

	def update(self, walls):

		keys = pygame.key.get_pressed()

		old_x, old_y = self.rect.topleft
		# Save the old position so we can undo
		# movement if the player hits a wall.

		#Horizontal movement
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed

		# Undo horizontal movement if blocked
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.x = old_x

		#Vertical movement
		if keys[pygame.K_UP]:
			self.rect.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.rect.y += self.speed

		# Undo vertical movement if blocked
		if pygame.sprite.spritecollide(self, walls, False):
			self.rect.y = old_y

#=======================================================================
#                           WALL CLASS
#=======================================================================

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                            ROCK CLASS
#=======================================================================

class Rocks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(LIGHT_GRAY)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                       LEFT WALL CLASS
#=======================================================================

class LeftWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          RIGHT WALL CLASS
#=======================================================================

class RightWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          TOP WALL CLASS
#=======================================================================

class TopWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                         BOTTOM WALL CLASS
#=======================================================================

class BottomWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                            LAND CLASS
#=======================================================================

class Land(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SAND)
        self.rect = self.image.get_rect(topleft = (x,y))










#=======================================================================
#                        SAND DOLLAR CLASS
#=======================================================================

class SandDollar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SAND)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                           BONE CLASS
#=======================================================================

class Bone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(LIGHT_GRAY)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          CORAL CLASS
#=======================================================================

class Coral(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(CORAL)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                        SEAWEED CLASS
#=======================================================================

class Kelp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft = (x,y))










#=======================================================================
#                        HELPFUl NPC CLASS
#=======================================================================

class HelpfulNPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                         TREASURE CLASS
#=======================================================================

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                            KEY CLASS
#=======================================================================

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          GAS TANK CLASS
#=======================================================================

class GasTank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SAND)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          WET SUIT CLASS
#=======================================================================

class WetSuit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(LIGHT_GRAY)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                            FIN CLASS
#=======================================================================

class Fins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(CORAL)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          SUB HULL CLASS
#=======================================================================

class SubHull(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                           PROPELLER CLASS
#=======================================================================

class Propeller(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                           RADAR CLASS
#=======================================================================

class Radar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x,y))









#=======================================================================
#                           SHARK CLASS
#=======================================================================

class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                           SQUID CLASS
#=======================================================================

class Squid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x,y))

#=======================================================================
#                           BOSS 1 CLASS
#=======================================================================

class BossOne(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x,y))
        
#=======================================================================
#                          BOSS 2 CLASS
#=======================================================================

class BossTwo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
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
        self.image.fill(GOLD)
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
#                        LOADING THE GAME
#=======================================================================

def load_maze(filename):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()

	player = None
	start_point = None
	wall = None
	rocks = None
	left_wall = None
	right_wall = None
	top_wall = None
	bottom_wall = None
	land = None

	sand_dollar = None
	bone = None
	coral = None
	kelp = None

	helpful_npc = None
	treasure = None
	key = None
	gas_tank = None
	wetsuit = None
	fin = None
	sub_hull = None
	propeller = None
	radar = None
	
	shark = None
	squid = None
	boss_one = None
	boss_two = None
	
	end_point = None

	with open (filename, "r") as file:
		maze_level = [line.strip() for line in file]

	for row_index, row in enumerate (maze_level):
			for col_index, char in enumerate (row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				
# The structural aspects of the game
				if char == "1":
					wall = Wall(x,y)
					all_sprites.add(wall)
					wall_sprites.add(wall)
				elif char == "S":
					start_point = StartPoint (x,y)
					player = Player (x,y)
					all_sprites.add (start_point)
					all_sprites.add(player)
				elif char == "S":
					rocks = Rocks(x, y)
					all_sprites.add(rocks)
					rocks_sprites.add(rocks)
				elif char == "L":
					left_wall = LeftWall(x, y)
					all_sprites.add(left_wall)
					left_wall_sprites.addleft_wall)
				elif char == "R":
					right_wall = RightWall(x, y)
					all_sprites.add(right_wall)
					right_wall_sprites.add(right_wall)
				elif char == "T":
					top_wall = TopWall(x, y)
					all_sprites.add(top_wall)
					top_wall_sprites.add(top_wall)
				elif char == "B":
					bottom_wall = BottomWall(x, y)
					all_sprites.add(bottom_wall)
					bottom_wall_sprites.add(bottom_wall)
				elif char == "E":
					land = Land(x, y)
					all_sprites.add(land)
					land_sprites.add(land)
					
# These are the collectable/decorative objects in the game
				elif char == "D":
					sand_dollar = SandDollar(x, y)
					all_sprites.add(sand_dollar)
					sand_dollar_sprites.add(sand_dollar)
				elif char == "N":
					bone = Bone(x, y)
					all_sprites.add(bone)
					bone_sprites.add(bone)
				elif char == "C":
					coral = Coral(x, y)
					all_sprites.add(coral)
					coral_sprites.add(coral)
				elif char == "K":
					kelp = Kelp(x, y)
					all_sprites.add(kelp)
					kelp_sprites.add(kelp)

#These are the interactive elements in the game
				elif char == "2":
					helpful_npc = HelpfulNPC(x, y)
					all_sprites.add(helpful_npc)
					helpful_npc_sprites.add(helpful_npc)
				elif char == "X":
					treasure = Treasure(x, y)
					all_sprites.add(treasure)
					treasure_sprites.add(treasure)
				elif char == "J":
					key = Key(x, y)
					all_sprites.add(key)
					key_sprites.add(key)
				elif char == "G":
					gas_tank = GasTank(x, y)
					all_sprites.add(gas_tank)
					gas_tank_sprites.add(gas_tank)
				elif char == "Y":
					wetsuit = Wetsuit(x, y)
					all_sprites.add(wetsuit)
					wetsuit_sprites.add(wetsuit)
				elif char == "F":
					fins = Fins(x, y)
					all_sprites.add(fins)
					fins_sprites.add(fins)
				elif char == "H":
					sub_hull = SubHull(x, y)
					all_sprites.add(sub_hull)
					sub_hull_sprites.add(sub_hull)
				elif char == "O":
					propeller = Propeller(x, y)
					all_sprites.add(propeller)
					propeller_sprites.add(propeller)
				elif char == "A":
					radar = Radar(x, y)
					all_sprites.add(radar)
					radar_sprites.add(radar)

#These are the enemies/antagonists in the game
				elif char == "I":
					shark = Shark(x, y)
					all_sprites.add(shark)
					shark_sprites.add(shark)
				elif char == "Q":
					squid = Squid(x, y)
					all_sprites.add(squid)
					squid_sprites.add(squid)
				elif char == "4":
					boss_one = BossOne(x, y)
					all_sprites.add(boss_one)
					boss_one_sprites.add(boss_one)
				elif char == "5":
					boss_two = BossTwo(x, y)
					all_sprites.add(boss_two)
					boss_two_sprites.add(boss_two)

#Endpoint
				elif char == "E":
					end_point = EndPoint (x,y)
					all_sprites.add(end_point)



	return all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point

def main():
	clock = pygame.time.Clock()
	keys = 0
	
	all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point = load_maze("LVL1.txt")
	running = True
	game_won = False

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Maze Game")

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
				
				if  pygame.sprite.collide_rect(player, end_point) and level == "1":
					screen.blit
					level = "2"
					all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point = load_maze(level + ".txt")
					print("level 2")
					player.speed = 3
				elif keys == 2 and pygame.sprite.collide_rect(player, end_point) and level == "2":
					screen.blit
					level = "3"
					print(level)
					all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point = load_maze(level + ".txt")
					print("Level 3")
		if pygame.sprite.spritecollide(player, enemy_sprites, False):
			all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point = load_maze(level + ".txt")
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
				all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, key, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, end_point = load_maze("maze" + level + ".txt")
				game_won = False

		#screen.blit(restart_text, restart_rect)
		 
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()

if __name__ == "__main__":
	main()
