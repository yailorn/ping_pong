from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __int__(self, sprite_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        virtual_surface.blit(self.image, (self.rect.x, self.rect.y))

WIDTH = 1200
HEIGHT = 700

ASPECT_RADIO = WIDTH / HEIGHT

back = (151, 228, 241)

window = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
display.set_mode("ping-pong")

clock = time.Clock()
fps = 60

virtual_surface = Surface((WIDTH, HEIGHT))
current_size = window.get_size()

ball = GameSprite("images/ball.png", 200, 200, 200, 200, 20)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
        if e.type == VIDEORESIZE:
            new_width = e.w
            new_height = int(new_width / ASPECT_RADIO)
            window = display.set_mode((new_height, new_width), RESIZABLE)
            current_size = window.get_size()

    virtual_surface.fill(back)

    ball.reset()

    scaled_surface = transform.scale(virtual_surface, current_size)
    window.blit(scaled_surface, (0, 0))

    display.update()
    clock.tick(fps)