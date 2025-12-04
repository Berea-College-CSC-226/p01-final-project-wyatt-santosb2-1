import pygame
import sys
import random

width,height = 400,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Wing Dash')

sky = "lightblue"
pipe_height = 500
score = 0
clock = pygame.time.Clock()
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()



        self.image = pygame.image.load("image/Flappy-Bird-PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.gravity = .8
        self.jump_force = -10
        self.velocity = 0

    def jump(self):
        self.velocity = self.jump_force

    def move(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class Pipe:
    def __init__(self,x,y,flipped = False):
        self.flipped = flipped


        self.colum = pygame.image.load("image/Bottom pipe.png").convert_alpha()
        self.colum = pygame.transform.scale(self.colum,(60,pipe_height))

        if self.flipped:
            self.colum = pygame.transform.flip(self.colum,False,True)

        self.rect = self.colum.get_rect()
        self.rect.topleft = (x,y)
        self.speed = 3

    def move(self):
        self.rect.x-= self.speed
    def draw(self,surface):
        surface.blit(self.colum,self.rect)

def main():
    clock = pygame.time.Clock()
    bird = Bird(50,250)

    pipes = []
    spawn_time = 0

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        bird.jump()
        bird.move()
        if bird.rect.bottom >= height:
            bird.rect.bottom = height


        spawn_time += 1
        if spawn_time > 72:
            gap_center = random.randrange(-50,350)
            gap_size = 150

            bottom_y = gap_center + (gap_size // 2)
            top_y = gap_center - (gap_size // 2) - 30

            pipes.append(Pipe(400,bottom_y + 150,flipped = False))
            pipes.append(Pipe(400,top_y - 300,flipped = True))
            spawn_time = 0

        window.fill(sky)
        bird.draw(window)


        for pipe in pipes:
            pipe.move()
            pipe.draw(window)

        pygame.display.update()

main()
pygame.quit()

