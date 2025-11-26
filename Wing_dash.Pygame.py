import pygame
import sys

width,height = 400,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Wing Dash')
clock = pygame.time.Clock()

sky = "lightblue"
class Bird:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.gravity = 0.8
        self.jump_force = -10
        self.velocity = 0



    def jump(self):
        self.velocity += self.jump_force

    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        pass


def main():
    clock = pygame.time.Clock()
    bird = Bird(50,250)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        bird.jump()
        bird.move()

        window.fill(sky)
        bird.draw(window)

        pygame.display.update()

main()
pygame.quit()

