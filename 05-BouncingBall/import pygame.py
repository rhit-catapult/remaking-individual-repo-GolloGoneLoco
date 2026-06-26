import pygame
import sys
import random


class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        # Move the ball
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off left/right walls
        if self.x - self.radius <= 0 or self.x + self.radius >= 300:
            self.speed_x *= -1

        # Bounce off top/bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= 300:
            self.speed_y *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()

    # Create a ball
    ball1 = Ball(
        screen,
        pygame.Color('red'),
        x=150,
        y=150,
        radius=20,
        speed_x=3,
        speed_y=2
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        ball1.move()
        ball1.draw()

        pygame.display.update()


main()
