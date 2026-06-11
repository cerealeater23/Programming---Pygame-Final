# Coin Collect
# Author: Elliott Tsui
# Date: May 19 2026
import random

# import time
import pygame

BLACK = (0, 0, 0)
MENU_COLOUR = (173, 235, 179)
NUMENEMY = 2
NUMCOINS = 15
speed = 5
# Initializes pygame and music
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600), pygame.SCALED, vsync=1)
# Scaled and vsync was taken from google
# Background image defined
bg_image = pygame.image.load("images/grass.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (800, 600))


# classifies a coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Defines what a coyn is and its properties
        self.image = pygame.image.load("images/coyn.webp")
        self.image = pygame.transform.scale_by(self.image, 0.02)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)


# Classifies player 1
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Defines what a player 1 is and its properties
        self.image = pygame.image.load("images/mariyo.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()
        self.score = 0
        self.x_vel = 0
        self.y_vel = 0
        self.enemy_hits = 0

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # Creates bouncing movement
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.x_vel = -self.x_vel
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel
        if self.rect.top >= HEIGHT:
            self.rect.top = HEIGHT
            self.y_vel = -self.y_vel
        if self.rect.bottom <= 0:
            self.rect.bottom = 0
            self.y_vel = -self.y_vel

    # Defines movement
    def go_left(self):
        self.x_vel = -speed
        self.y_vel = 0

    def go_right(self):
        self.x_vel = speed
        self.y_vel = 0

    def go_down(self):
        self.y_vel = speed
        self.x_vel = 0

    def go_up(self):
        self.y_vel = -speed
        self.x_vel = 0


# Classifies player 2
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Defines what a player 2 is and its properties
        self.image = pygame.image.load("images/lewigi.png")
        self.image = pygame.transform.scale_by(self.image, 0.15)
        self.rect = self.image.get_rect()
        self.score = 0
        self.x_vel = 0
        self.y_vel = 0
        self.enemy_hits = 0

    # Defines movement
    def go_left(self):
        self.x_vel = -speed
        self.y_vel = 0

    def go_right(self):
        self.x_vel = speed
        self.y_vel = 0

    def go_up(self):
        self.y_vel = -speed
        self.x_vel = 0

    def go_down(self):
        self.y_vel = speed
        self.x_vel = 0

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # Creates bouncing movement
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.x_vel = -self.x_vel
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel
        if self.rect.top >= HEIGHT:
            self.rect.top = HEIGHT
            self.y_vel = -self.y_vel
        if self.rect.bottom <= 0:
            self.rect.bottom = 0
            self.y_vel = -self.y_vel


# Classifies an enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/gomba.webp")
        self.image = pygame.transform.scale_by(self.image, 0.07)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT + 1)
        self.y_vel = random.randrange(3, 5)
        self.x_vel = random.randrange(3, 5)

    def update(self):
        self.rect.x += self.x_vel
        # Creates bouncing movement
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.x_vel = -self.x_vel
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel
        self.rect.y += self.y_vel
        if self.rect.top >= HEIGHT:
            self.rect.top = HEIGHT
            self.y_vel = -self.y_vel
        if self.rect.bottom <= 0:
            self.rect.bottom = 0
            self.y_vel = -self.y_vel


# CONSTANTS
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)


# Defines the menu
def menu(screen: pygame.Surface, clock: pygame.time.Clock) -> str:
    pygame.font.init()
    pygame.mixer.music.stop()  # Just incase the player goes back to the menu after playing
    arial_font = pygame.font.SysFont("Arial", 22)
    menu_text = arial_font.render("Would you like to play?", True, BLACK)
    options_text = arial_font.render(
        "Hit 1 to play by yourself and practice, hit 2 to play with a friend, and hit ESC to stop!",
        True,
        BLACK,
    )
    # ------------ MENU LOOP
    while True:
        # ------ MAIN EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # User presses RED X
                return "done"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "practice_game"
                if event.key == pygame.K_2:
                    return "duo_game"
                if event.key == pygame.K_ESCAPE:
                    return "done"
        # ------ DRAWING TO SCREEN
        screen.fill(MENU_COLOUR)  # Background
        # Draws menu text
        screen.blit(
            menu_text,
            (
                (WIDTH // 2 - menu_text.width // 2),
                (HEIGHT // 2 - menu_text.height // 2 - 30),
            ),
        )
        # Draws options text
        screen.blit(
            options_text,
            (
                (WIDTH // 2 - options_text.width // 2),
                (HEIGHT // 2 - options_text.height // 2 - 5),
            ),
        )
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(120)  # 120 fps


def duo_game(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.mixer.init()
    # Constants
    arial_font = pygame.font.SysFont("Arial", 23)
    player1 = Player1()
    player2 = Player2()
    # Draws score
    player1_score = arial_font.render((f"Player 1 score: {player1.score}"), True, BLACK)
    player2_score = arial_font.render((f"Player 2 score: {player2.score}"), True, BLACK)
    player1_enemy_hits = arial_font.render(
        (f"Player 1 enemy hits: {player1.enemy_hits}"), True, BLACK
    )
    player2_enemy_hits = arial_font.render(
        (f"Player 2 enemy hits: {player2.enemy_hits}"), True, BLACK
    )
    # Sounds
    pygame.mixer.music.load("sounds/bensound-rumble.mp3")
    pygame.mixer.music.set_volume(0.5)
    coin_collected_sound = pygame.mixer.Sound("sounds/coin_collected_sound.mp3")
    coin_collected_sound.set_volume(1)
    damage_taken_sound = pygame.mixer.Sound("sounds/damage.mp3")
    # ---- Sprite Groups
    all_sprites = pygame.sprite.Group()
    coin_sprites = pygame.sprite.Group()
    enemy_sprite = pygame.sprite.Group()
    # Spawns enemies
    for _ in range(NUMENEMY):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprite.add(enemy)
    # Spawns coins
    for _ in range(NUMCOINS):
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)
    all_sprites.add(player1)
    all_sprites.add(player2)
    # Plays the background music
    pygame.mixer.music.play(loops=1, fade_ms=1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # User presses RED X
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.KEYDOWN:
                # WASD movements
                if event.key == pygame.K_a:
                    player1.go_left()
                if event.key == pygame.K_d:
                    player1.go_right()
                if event.key == pygame.K_w:
                    player1.go_up()
                if event.key == pygame.K_s:
                    player1.go_down()
                # Arrow key movements
                if event.key == pygame.K_LEFT:
                    player2.go_left()
                if event.key == pygame.K_RIGHT:
                    player2.go_right()
                if event.key == pygame.K_UP:
                    player2.go_up()
                if event.key == pygame.K_DOWN:
                    player2.go_down()
        # Exits if player 1 or player 2 gets hit 5 times
        if player1.enemy_hits == 5:
            print(f"Player 1 has died! Player 2 has won with {player2.score} coins!")
            return
        if player2.enemy_hits == 5:
            print(f"Player 2 has died! Player 1 has won with {player1.score} coins!")
            return
        # ------ GAME LOGIC
        all_sprites.update()
        coins_collided = pygame.sprite.spritecollide(player1, coin_sprites, True)
        # Updates and draws player 1 score and enemy hits
        for _ in coins_collided:
            player1.score += 1
            player1_score = arial_font.render(
                (f"Player 1 score: {player1.score}"), True, BLACK
            )
            print(f"Player 1 score: {player1.score}")
            coin_collected_sound.play()
        enemy_collided = pygame.sprite.spritecollide(player1, enemy_sprite, True)
        for _ in enemy_collided:
            player1.enemy_hits += 1
            damage_taken_sound.play()
            player1_enemy_hits = arial_font.render(
                (f"Player 1 enemy hits: {player1.enemy_hits}"), True, BLACK
            )
            print(
                f"Player 1 hit an enemy! They have hit an enemy {player1.enemy_hits} times!"
            )
        # Updates and draws player 2 score and enemy hits
        coins_collided = pygame.sprite.spritecollide(player2, coin_sprites, True)
        for _ in coins_collided:
            player2.score += 1
            coin_collected_sound.play()
            player2_enemy_hits = arial_font.render(
                (f"Player 2 enemy hits: {player2.enemy_hits}"), True, BLACK
            )
            print(f"Player 2 score: {player2.score}")
        enemy_collided = pygame.sprite.spritecollide(player2, enemy_sprite, True)
        for _ in enemy_collided:
            player2.enemy_hits += 1
            damage_taken_sound.play()
            player2_enemy_hits = arial_font.render(
                (f"Player 2 enemy hits: {player2.enemy_hits}"), True, BLACK
            )
            print(
                f"Player 2 hit an enemy! They have hit an enemy {player2.enemy_hits} times!"
            )
        # If all coins are gone: respawns all coins and enemies
        if not coin_sprites:
            for _ in range(NUMCOINS):
                coin = Coin()
                all_sprites.add(coin)
                coin_sprites.add(coin)
            for _ in range(NUMENEMY):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemy_sprite.add(enemy)
        # ------ DRAWING TO SCREEN
        # Draws background image
        screen.blit(bg_image, (0, 0))
        # Draws score
        screen.blit(
            player2_score,
            (
                (WIDTH - player2_score.width),
                (0),
            ),
        )
        screen.blit(
            player1_score,
            (
                (0),
                (0),
            ),
        )
        # Draws enemy hits
        screen.blit(
            player2_enemy_hits,
            (
                (WIDTH - player2_enemy_hits.width),
                (550),
            ),
        )
        screen.blit(
            player1_enemy_hits,
            (
                (0),
                (550),
            ),
        )
        all_sprites.draw(screen)
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(120)  # 120 fps


# Solo game
def practice_game(screen: pygame.Surface, clock: pygame.time.Clock):
    arial_font = pygame.font.SysFont("Arial", 23)
    pygame.mixer.init()
    player1 = Player1()
    # Draws Player 1 score and enemy hits
    player1_score = arial_font.render((f"Player 1 score: {player1.score}"), True, BLACK)
    player1_enemy_hits = arial_font.render(
        (f"Player 1 enemy hits: {player1.enemy_hits}"), True, BLACK
    )
    # Loads all the sounds
    pygame.mixer.music.load("sounds/bensound-rumble.mp3")
    pygame.mixer.music.set_volume(0.5)
    coin_collected_sound = pygame.mixer.Sound("sounds/coin_collected_sound.mp3")
    coin_collected_sound.set_volume(1)
    damage_taken_sound = pygame.mixer.Sound("sounds/damage.mp3")
    # ---- Sprite Groups
    all_sprites = pygame.sprite.Group()
    coin_sprites = pygame.sprite.Group()
    enemy_sprite = pygame.sprite.Group()
    # Draws enemies
    for _ in range(NUMENEMY):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprite.add(enemy)
    # Draws coins
    for _ in range(NUMCOINS):
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)
    # Adds player 1 to the sprite group
    all_sprites.add(player1)

    pygame.mixer.music.play(loops=1, fade_ms=1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # User presses RED X
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            # WASD movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.go_left()
                if event.key == pygame.K_d:
                    player1.go_right()
                if event.key == pygame.K_w:
                    player1.go_up()
                if event.key == pygame.K_s:
                    player1.go_down()
        # Exits if player 1 gets hit 5 times
        if player1.enemy_hits == 5:
            print(f"You have died with a score of {player1.score}!")
            return
        # ------ GAME LOGIC
        all_sprites.update()
        coins_collided = pygame.sprite.spritecollide(player1, coin_sprites, True)
        for _ in coins_collided:
            player1.score += 1
            player1_score = arial_font.render(
                (f"Player 1 score: {player1.score}"), True, BLACK
            )
            print(f"Player 1 score: {player1.score}")
            coin_collected_sound.play()
        enemy_collided = pygame.sprite.spritecollide(player1, enemy_sprite, True)
        for _ in enemy_collided:
            player1.enemy_hits += 1
            damage_taken_sound.play()
            player1_enemy_hits = arial_font.render(
                (f"Player 1 enemy hits: {player1.enemy_hits}"), True, BLACK
            )
            print(
                f"Player 1 hit an enemy! They have hit an enemy {player1.enemy_hits} times!"
            )
        if not coin_sprites:
            for _ in range(NUMCOINS):
                coin = Coin()
                all_sprites.add(coin)
                coin_sprites.add(coin)
            for _ in range(NUMENEMY):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemy_sprite.add(enemy)
        # ------ DRAWING TO SCREEN
        screen.blit(bg_image, (0, 0))
        # Draws player score
        screen.blit(
            player1_score,
            (
                (0),
                (0),
            ),
        )
        screen.blit(
            player1_enemy_hits,
            (
                (0),
                (550),
            ),
        )
        all_sprites.draw(screen)
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(120)  # 60 fps


def main():

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("2 Player Coin Collect")

    # Variables
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while True:
        choice = menu(screen, clock)
        if choice == "done":
            break
        elif choice == "duo_game":
            duo_game(screen, clock)
        elif choice == "practice_game":
            practice_game(screen, clock)

    pygame.quit()


if __name__ == "__main__":
    main()
