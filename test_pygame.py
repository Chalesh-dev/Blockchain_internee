import random
import pygame


class MainGame:
    def __init__(self):
        self.screen_game = ScreenGame()
        self.tank = Tank(self.screen_game)
        self.gun = Gun(self.screen_game)
        self.air_plane = Airplane(self.screen_game,self.gun)
        self.score = Score(self.screen_game)
        self.player = Player(self.screen_game , self.tank , self.life)
        self.life = Life(self.screen_game)


class ScreenGame:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.grid_size = 15
        self.black = (0, 0, 0)

    def run_screen(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.black)
        pygame.display.flip()
        pygame.time.Clock().tick(30)


class Tank():
    def __init__(self, screen):
        self.screen = screen
        self.positions = [(screen.width // 0, screen.height // 2)]
        self.direction_left = (-1, 0)
        self.direction_right = (1, 0)
        self.direction = random.choice((self.direction_left, self.direction_right))

    def get_head_position(self):
        return self.positions[0]

    def render(self, surface):
        for i in self.positions:
            pygame.draw.rect(surface, (0, 102, 0), (i[0], i[1], self.screen.grid_size, self.screen.grid_size))


class Gun(Tank):
    def __init__(self, screen):
        super().__init__(screen)
        self.size_bullet = self.screen.grid_size // 2
        self.bullets = []

    def bullet_show(self):
        for j in self.positions:
            pygame.draw.rect(self.screen, (255, 0, 0), (j[0], j[1], self.size_bullet, self.size_bullet))
    def shot_bullet(self,x,y):
        bullet = Bullet(x,y)
        self.bullets.append(bullet)
    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move()


class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 15
        self.speed = 10

    def move(self):
        self.y -= self.speed


class Airplane():
    def __init__(self, screen, gun):
        self.gun = gun
        self.screen = screen
        self.position = (0, 0)
        self.randomize_position()
        self.fire_rate = 2
        self.fire_delay = 30


    def randomize_position(self):
        self.position = ((random.randint(0, self.screen.width - self.screen.grid_size) // self.screen.grid_size) * self.screen.grid_size,
                        random.randint(0, (self.screen.height // 2 - self.screen.grid_size) // self.screen.grid_size) * self.screen.grid_size)
    def render(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.position[0], self.position[1]), self.screen.grid_size,self.screen.grid_size)

    def del_airplane(self):
        for kill in self.position:
            if self.position == self.gun.shoot_tank():
                [kill].pop(0)
    def shoot_air_plane(self,level):
        if self.fire_delay == 0:
            bullet_x = self.position[0] + self.screen.grid_size // 2
            bullet_y = self.position[1] + self.screen.grid_sizse
            self.gun.shot_bullet(bullet_x, bullet_y)
            self.fire_delay = 30
        else:
            self.fire_delay -= 1

class planeMod(Airplane):
    def __init__(self,screen,gun,level):
        super().__init__(screen,gun)
        self.level == level

    # def live(self):
    #






class Player():
    def __init__(self,screen , tank , life , font_size =100):
        self.screen = screen
        self.tank = tank
        self.life = life
        self.font = pygame.font.Font(None, font_size)
    def handle_shoot_tank(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            tank_x, tank_y = self.tank.positions[0]
            bullet_x = tank_x + self.screen.grid_size // 4
            bullet_y = tank_y
            self.tank.bullets.append((bullet_x, bullet_y))
        for bullet in self.tank.bullets:
            bullet_x, bullet_y = bullet
            bullet_y -= 5
            bullet = (bullet_x, bullet_y)
        self.tank.bullets = [bullet for bullet in self.tank.bullets if bullet[1] > 0]
    def handle_tank(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.tank.direction = self.tank.direction_left
        elif keys[pygame.K_RIGHT]:
            self.tank.direction = self.tank.direction_right
    def reduce_life(self,x,y):
        if self.life.Decrease == 0:
            text = self.font.render(f"GAME OVER!", True, (0, 255, 0))
            self.screen.bilt(text, (x, y))

class Score():
    def __init__(self ,screen, font_size = 36):
        self.screen =  screen
        self.value = 0
        self.font = pygame.font.Font(None,font_size)
    def increase(self,points=1):
        self.value += points
    def show_score(self, x , y):
        text = self.font.render(f'SCore:{self.value}',True ,(255,255,0))
        self.screen.bilt(text,(x,y))

class Life():
    def __init__(self , screen , font_size = 36):
        self.screen = screen
        self.value = 1
        self.font = pygame.font.Font(None , font_size)
    def Decrease(self,life=100):
        self.value -= life
    def show_life(self, x, y):
        text = self.font.render(f'life:{self.value}', True, (0, 255, 0))
        self.screen.bilt(text, (x, y))