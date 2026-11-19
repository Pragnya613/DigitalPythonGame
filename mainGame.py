import pygame, random

pygame.init()

#=======================================================================
#                            CONSTANTS
#=======================================================================

TILE_SIZE = 20
WIDTH     = 50 * TILE_SIZE
HEIGHT    = 30 * TILE_SIZE
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

GOLD       = (255, 210, 40)
SAND       = (227, 194, 138)
LIGHT_GRAY = (176, 169, 158)
GREEN      = (43, 84, 53)
CORAL      = (214, 120, 155)

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
		self.health = 50
		self.lives = 3
		self.inventory_size = 3
        self.move = True

#=======================================================================
#  Here is the player's inventory which contains all of the items that 
# they'll use in the game. These items will be bought at the store using
#        the sand dollars that they collect in level one.
#=======================================================================
		self.inventory = {
			"Sand Dollar": sandDollar
			"Bones"      : bones
			"Gas Tank"   : gasTank
			"Wet Suit"   : wetSuit
			"Fins"       : finsV
			"Sub Hull"   : subHull
			"Propeller"  : propellerV 
			"Radar"      : radarV
			}
			
	def add_item(self, item):
		if len(self.inventory) < self.inventory_size:
            self.inventory.append(item)
        else:
            print("Inventory full! Cannot add", item)
            
    def use_item(self, index):
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            if item == "Potion" and self.health < self.max_health:
                self.health = min(self.max_health, self.health + 20)
                print("Used Potion! Health:", self.health)
                del self.inventory[index]
	
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
#                          STORE WALL CLASS
#=======================================================================

class StoreWall(pygame.sprite.Sprite):
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
#                            LAVA CLASS
#=======================================================================

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GOLD)
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
        self.image = pygame.image.load("clownfish.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize to fit tile
        self.rect = self.image.get_rect(topleft = (x,y))
   
		self.dialog_active = False
		self.dialog_index = 0
		self.dialog_lines = [
		"Clownfish: Hello there!",
		"Player: Hi!",
		"Clownfish: What are you looking for?",
		"Player: I need more tools to dive deeper into the ocean. Could you help me find those?",
		"Clownfish: Of Course!",
		"Clownfish: In order to get better equipment, go to the store to buy or upgrade your supplies!",
		"Player: Wait, but how would I pay to get better technology?",
		"Clownfish: Did you notice the sand dollars when you arrived here?",
		"Player: Yes . . . ?",
		"Clownfish: Collect those sand dollars in order to be able to buy more things and upgrade your abilities!",
		"Player: Wow! Thanks for all your help!",
		"Clownfish: Wait! Before you leave, here's 5 sand dollars to help you get started and good luck!",
		"Player: Thank you!"
		]
        
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
        self.image = pygame.image.load("shark.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize to fit tile
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
#                          START CLASSES
#=======================================================================

class StartPoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface(
            (TILE_SIZE, TILE_SIZE)
        )
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft=(x, y))
        
#=======================================================================
#                        LOADING THE GAME
#=======================================================================

def load_maze(game):
	all_sprites = pygame.sprite.Group()
	wall_sprites = pygame.sprite.Group()
	rocks_sprites = pygame.sprite.Group()
	left_wall_sprites = pygame.sprite.Group()
	right_wall_sprites = pygame.sprite.Group()
	top_wall_sprites = pygame.sprite.Group()
	bottom_wall_sprites = pygame.sprite.Group()
	store_wall_sprites = pygame.sprite.Group()
	land_sprites = pygame.sprite.Group()
	lava_sprites = pygame.sprite.Group()
	
	sand_dollar_sprites = pygame.sprite.Group()
	bone_sprites = pygame.sprite.Group()
	coral_sprites = pygame.sprite.Group()
	kelp_sprites = pygame.sprite.Group()
	
	helpful_npc_sprites = pygame.sprite.Group()
	treasure_sprites = pygame.sprite.Group()
	key_sprites = pygame.sprite.Group()
	gas_tank_sprites = pygame.sprite.Group()
	wetsuit_sprites = pygame.sprite.Group()
	fins_sprites = pygame.sprite.Group()
	sub_hull_sprites = pygame.sprite.Group()
	propeller_sprites = pygame.sprite.Group()
	radar_sprites = pygame.sprite.Group()
	
	shark_sprites = pygame.sprite.Group()
	squid_sprites = pygame.sprite.Group()
	boss_one_sprites = pygame.sprite.Group()
	boss_two_sprites = pygame.sprite.Group()

	player = None
	wall = None
	start_point = None
	rocks = None
	left_wall = None
	right_wall = None
	top_wall = None
	bottom_wall = None
	store_wall = None
	land = None
	lava = None

	sand_dollar = None
	bone = None
	coral = None
	kelp = None

	helpful_npc = None
	treasure = None
	key = None
	gas_tank = None
	wetsuit = None
	fins = None
	sub_hull = None
	propeller = None
	radar = None
	
	shark = None
	squid = None
	boss_one = None
	boss_two = None
	
	with open (game, "r") as file:
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
				elif char == "P":
					start_point = StartPoint (x,y)
					player = Player(x,y)
					all_sprites.add (start_point)
					all_sprites.add(player)
				elif char == "S":
					rocks = Rocks(x, y)
					all_sprites.add(rocks)
					rocks_sprites.add(rocks)
				elif char == "L":
					left_wall = LeftWall(x, y)
					all_sprites.add(left_wall)
					left_wall_sprites.add(left_wall)
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
				elif char == "Z":
					store_wall = StoreWall(x, y)
					all_sprites.add(store_wall)
					store_wall_sprites.add(store_wall)
				elif char == "E":
					land = Land(x, y)
					all_sprites.add(land)
					land_sprites.add(land)
				elif char == "M":
					lava = Lava(x, y)
					all_sprites.add(lava)
					lava_sprites.add(lava)
					
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

	return all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, land, lava, sand_dollar, bone, coral, kelp, helpful_npc, treasure, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, boss_one, boss_two

#=======================================================================
#     Here is the main function that has all the code to actually 
#    use the sprites, display the graphics, and allow the player to 
#                      actually play the game.
#=======================================================================

def main():
	clock = pygame.time.Clock()
	zone = "1"
	
	# Here are the collectables that allow the player to either advance 
	# to the next level or attain items to advance to the next level
	key = 0

#=======================================================================
# Loading the first level of the game in and creating the display where 
# 					the game will actually appear.
#=======================================================================

	all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, helpful_npc, treasure, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, boss_one, boss_two = load_maze("map" + zone + ".txt")
	running = True
	game_won = False

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Ocean Game")

	while running:
		player.update(wall_sprites)
		for event in pygame.event.get():
			
			#Allows the player to leave the game
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r and game_won:
					player.rect.topleft = start_point.rect.topleft
					game_won = False
			   keys = pygame.key.get_pressed()

		if player.move:
			if keys[pygame.K_LEFT]:
				player.rect.x -= 1
			if keys[pygame.K_RIGHT]:
				player.rect.x += 1
			if keys[pygame.K_UP]:
				player.rect.y -= 1
			if keys[pygame.K_DOWN]:
				player.rect.y += 1

#=======================================================================
# 			This code below starts the dialogue for the npc
#=======================================================================

		if player.rect.colliderect(npc) and not dialog_active:
			if keys[pygame.K_s]:
				dialog_active = True
				player.move = False
				dialog_index = 0

		# Advance dialog with SPACE
		if dialog_active and keys[pygame.K_SPACE]:
			dialog_index += 1
			pygame.time.wait(200)

			if dialog_index >= len(dialog_lines):
				dialog_active = False
				player.move = True
				# Give item at end of dialog
				player.add_item("Potion")
				# Push player away
				if player.rect.colliderect(npc):
					player.rect.y = npc.top - player.rect.height - 10

		# Toggle inventory with I
		if keys[pygame.K_i]:
			show_inventory = not show_inventory
			pygame.time.wait(200)  # debounce

		# Use item with number keys
		for i in range(1, 10):
			if keys[getattr(pygame, f"K_{i}")]:
				player.use_item(i-1)
				pygame.time.wait(200)

		# Drawing
		screen.fill(WHITE)
		pygame.draw.rect(screen, BLUE, player.rect)
		pygame.draw.rect(screen, GREEN, npc)

		# Health bar / menu bar
		pygame.display.set_caption("Health: " + str(player.health) + "/" + str(player.max_health))
		#health_text = font.render(f"Health: {player.health}", True, BLACK)
		#screen.blit(health_text, (10, 10))

		# Dialog
		if dialog_active and dialog_index < len(dialog_lines):
			text = font.render(dialog_lines[dialog_index], True, BLACK)
			screen.blit(text, (50, 280))

		# Inventory
		if show_inventory:
			inv_text = font.render("Inventory:", True, BLACK)
			screen.blit(inv_text, (350, 10))
			for idx, item in enumerate(player.inventory):
				item_text = font.render(f"{idx+1}: {item}", True, BLACK)
				screen.blit(item_text, (350, 40 + idx*30))

			if not game_won:
				#Change this to once the 
				if pygame.sprite.collide_rect(player, right_wall) or pygame.sprite.collide_rect(player, bottom_wall) and zone == "9": #Once the player collides with one of the walls in zone 9, move onto the next level
					screen.blit
					
					#Setting the level to 2 and loading in the next level of the game
					zone = "2"
					all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, helpful_npc, treasure, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, boss_one, boss_two = load_maze("level" + zone + ".txt")
					
					#Indicates the start of the next level
					text = font.render("LEVEL 2", True, GOLD)
					text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))

					background = text_rect.inflate(30, 20)
					pygame.draw.rect(screen, BLACK, background)
					screen.blit(text, text_rect)

				elif pygame.sprite.collide_rect(player, end_point) and level == "2": #Once the player meets the endpoint in level two, move on to the last level
					screen.blit
					
					#Setting the level to 3 and loading in the last level of the game
					zone = "3"
					all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, helpful_npc, treasure, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, boss_one, boss_two = load_maze("level" + zone + ".txt")

					#Indicates the start of the last level
					text = font.render("LEVEL 3", True, GOLD)
					text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))

					background = text_rect.inflate(30, 20)
					pygame.draw.rect(screen, BLACK, background)
					screen.blit(text, text_rect)
					
#=======================================================================
#			    Collecting Sand Dollars for Currency
#=======================================================================

			if pygame.sprite.collide_rect(player, sand_dollar_sprites, False):
				sandDollars += 1
				
#=======================================================================
#				   Event: Player Runs into an NPC
#=======================================================================
			
			if pygame.sprite.collide(player, helpful_npc_sprites, False):

					
#=======================================================================
#				         Health and Lives System
#=======================================================================
# The player starts with 50 health and every time they collide with a 
#     rock, a shark, or a squid, they lose a bit of their health.
#    Once they lose all their health, they lose one of their 3 lives
#      This pattern continues until the player either loses all
#		      their lives or if they find the treasure.

			if pygame.sprite.collide_rect(player, rocks_sprites, False):
				player.health -= 1
				print(health)
				if player.health < 1:
					player.lives -= 1
					print(player.lives)
					player.health = 50
			if pygame.sprite.collide_rect(player, shark_sprites, False):
				player.health -= 3
				print(player.health)
				if player.health < 1:
					player.lives -= 1
					print(player.lives)
					player.health = 50
			if pygame.sprite.collide_rect(player, squid_sprites):
				player.health -= 5
				print(player.health)
				if player.health < 1:
					player.lives -= 1
					print(player.lives)
					player.health = 50
					
#=======================================================================
#				         Collecting Keys
#=======================================================================
					
			if pygame.sprite.collide_rect(player, key_sprites):
				key += 1

#=======================================================================
#				      Buying items from the Store
#=======================================================================
			if pygame.sprite.collide_rect(player, 

#=======================================================================
#				     Upgrading items in the Store
#=======================================================================

			if pygame.sprite.collide_rect(player, store_wall):
				

#=======================================================================
#				         Winning the Game
#=======================================================================

		if health > 1 and lives > 0 and pygame.sprite.collide_rect(player, treasure):
			print("You Win!")
			game_won = True
				
		screen.fill(WHITE)
		all_sprites.draw(screen)
		
		if game_won == True:
			text = font.render("Great Job on finding the treasure!", True, GOLD)
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
				all_sprites, wall_sprites, player, start_point, rocks, left_wall, right_wall, top_wall, bottom_wall, sand_dollar, bone, coral, kelp, helpful_npc, treasure, gas_tank, wetsuit, fins, sub_hull, propeller, radar, shark, squid, boss_one, boss_two, end_point = load_maze("maze" + level + ".txt")
				game_won = False

		#screen.blit(restart_text, restart_rect)
		 
		pygame.display.flip()
		clock.tick(FPS)

#=======================================================================
#				        Ends the Function
#=======================================================================

	pygame.quit()

if __name__ == "__main__":
	main()
