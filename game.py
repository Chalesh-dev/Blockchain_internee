import pygame
import random
import sys

GRID_SIZE = 20
WIDTH = 600
HEIGHT = 400

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)


class Snake:
    def __init__(self):
        self.size = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        current_head = self.get_head_position()
        x, y = self.direction
        new_head = ((current_head[0] + x * GRID_SIZE) % WIDTH, (current_head[1] + y * GRID_SIZE) % HEIGHT)
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            self.rest()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.size:
                self.positions.pop()

    def rest(self):
        self.size = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for s in self.positions:
            pygame.draw.rect(surface, SNAKE_COLOR, (s[0], s[1], GRID_SIZE, GRID_SIZE))


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, FOOD_COLOR, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))


class SnakeGame:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def handle(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction != DOWN:
            self.snake.direction = UP
        elif keys[pygame.K_DOWN] and self.snake.direction != UP:
            self.snake.direction = DOWN
        elif keys[pygame.K_LEFT] and self.snake.direction != RIGHT:
            self.snake.direction = LEFT
        elif keys[pygame.K_RIGHT] and self.snake.direction != LEFT:
            self.snake.direction = RIGHT

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle()
            self.snake.update()
            if self.snake.get_head_position() == self.food.position:
                self.snake.size += 1
                self.food.randomize_position()
            screen.fill((0, 0, 0))
            self.snake.render(screen)
            self.food.render(screen)
            pygame.display.flip()
            clock.tick(10)


if __name__ == "__main__":
    SnakeGame().run()
