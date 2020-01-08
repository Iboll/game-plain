import sys
import os
import pygame
import random

kills = 0
hearts = 5
fps = 60
pygame.init()
clock = pygame.time.Clock()
z_width = 1000
z_height = 900
sscreen = pygame.display.set_mode((z_width, z_height))
pygame.display.set_caption("PILOTS'S WAR")
# Размеры и сам стартовый экран
pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/rb.mp3')
pygame.mixer.music.play()


# Музыка для стартового экрана


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image = image.convert()
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


# Функции загрузки картинок


def terminate():
    pygame.quit()
    sys.exit()


# Стартовый экран
def start_screen():
    intro_text = ["PILOTS'S WAR", "",
                  "w-forward",
                  "a-leftward",
                  "s-backward",
                  "d-rightward",
                  "LBM-shoot", "",
                  "You have 5 hearts.",
                  "If the enemy crosses the border,",
                  "you will lose 1 heart",
                  "Good luck! Have fun!", "", "",
                  "Press anywhere to continue"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (z_width, z_height))
    sscreen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 400
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sscreen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                return
                # Начало самой игры
        pygame.display.flip()
        clock.tick(fps)


# Финальный экран
def final_screen():
    # Музыка финального экрана
    pygame.mixer.music.stop()
    pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/die.mp3')
    pygame.mixer.music.play()
    intro_text = [f"You killed {kills} enemies",
                  f"Good job, pilot!",
                  f"Press anywhere to restart"]

    fon = pygame.transform.scale(load_image('final.jpg'), (1200, 900))
    sscreen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 500
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sscreen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/mot.mp3')
                pygame.mixer.music.play()
                return
        pygame.display.flip()
        clock.tick(fps)


start_screen()
# Размеры и сам экран игры
width = 1200
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PILOTS'S WAR")
plain_sprites = pygame.sprite.Group()
y_fon = 0


# Функция, имитирующая выстрелы
def sho_v():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/rb.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/mot.mp3')
    pygame.mixer.music.play()


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("plain1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 700

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.rect.x != 60:
                self.rect.x -= 10
        if keys[pygame.K_d]:
            if self.rect.x != 940:
                self.rect.x += 10
        if keys[pygame.K_w]:
            if self.rect.y != 100:
                self.rect.y -= 10
        if keys[pygame.K_s]:
            if self.rect.y != 700:
                self.rect.y += 10
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.shoot(self.rect.x, self.rect.y)
            sho_v()

    def shoot(self, x, y):
        s = Shots(x, y)
        shots.add(s)
        # Выстрел


# Класс противника
class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("plain2.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(60, 940)
        self.rect.y = random.randrange(-250, -100)

    def update(self):
        global hearts
        global kills
        self.rect.y += 12
        if self.rect.y > height:
            self.kill()
            # Функция для очистки того, что находится за экраном
            hearts -= 1
        dies = pygame.sprite.groupcollide(enemies, shots, True, True)
        for plain in dies:
            Enemy.kill(plain)
            kills += 1


# Класс выстрелов
class Shots(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x + 96
        self.rect.y = y

    def update(self):
        self.rect.y -= 15
        if self.rect.y < 0:
            self.kill()
        # Функция для очистки того, что находится за экраном


# Класс фона экрана
class Fon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

    def update(self, *args):
        global y_fon
        if y_fon == height:
            y_fon = 0
            y_fon += 4
        else:
            y_fon += 4
        # Происходит дефолтное движение
        fon = pygame.transform.scale(load_image('grees.jpg'), (width, height))
        screen.blit(fon, (0, y_fon - height))
        screen.blit(fon, (0, y_fon))
        plain_sprites.draw(screen)


f = pygame.font.Font(None, 50)
pl = Player(plain_sprites)
f_sprites = pygame.sprite.Group()
fn = Fon(f_sprites)
shots = pygame.sprite.Group()
enemies = pygame.sprite.Group()
f_sprites.add(pl)
# Спрайты

# Музыка для игры
pygame.mixer.music.load('C:/Users/Soltan/PycharmProjects/game-plain/data/mot.mp3')
pygame.mixer.music.play()

running = True
timing = 0
while running:
    clock.tick(fps)
    if hearts <= 0:
        enemies.empty()
        shots.empty()
        final_screen()
        kills = 0
        hearts = 5
        pl.rect.x = 500
        pl.rect.y = 700
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        plain_sprites.update(event)
    f_sprites.update()
    shots.update()
    timing += clock.tick()
    if timing > 6000:
        timing = 0
        for i in range(random.randrange(1, 9)):
            enem = Enemy(enemies)
            s = pygame.sprite.Group()
            s.add(enem)
            die = pygame.sprite.groupcollide(s, enemies, True, True)
            for j in die:
                Enemy.kill(j)
            enemies.add(enem)
            s.empty()
    text = f.render(f'{str(kills)}-kills', 1, pygame.Color('red'))
    text2 = f.render(f'{str(hearts)}-hearts', 1, pygame.Color('red'))
    enemies.update()
    enemies.draw(screen)
    shots.draw(screen)
    screen.blit(text, (15, 15))
    screen.blit(text2, (1050, 15))
    pygame.display.flip()
pygame.quit()
