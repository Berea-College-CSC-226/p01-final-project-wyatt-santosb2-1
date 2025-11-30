import pygame
import sys

width,height = 400,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Wing Dash')

sky = "lightblue"
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()



        self.image = pygame.image.load("image/Flappy-Bird-PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.gravity = 0.8
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
    def __init__(self,x,gap_y,gap_height=150):
        self.x = x
        self.width = 50

        self.gap_y = gap_y
        self.gap_height = gap_height

        self.top_colum = pygame.Rect(x,0,self.width,self.gap_height)

        self.bottom_colum = pygame.Rect(x,0,self.width,self.gap_height)


        self.speed = 3
    def move(self):
        pass
    def draw(self,surface):
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
                if event.key == pygame.K_SPACE:
                        bird.jump()
        bird.move()
        if bird.rect.bottom >= height:
            bird.rect.bottom = height



        window.fill(sky)
        bird.draw(window)

        pygame.display.update()

main()
pygame.quit()

