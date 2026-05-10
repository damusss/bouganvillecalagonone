import pygame

win = pygame.Window("Icon Maker", (800, 800))
SIZE = 128


def make_circle(surf: pygame.Surface):
    medium = pygame.Surface(surf.size, pygame.SRCALPHA)
    medium.fill(0)
    pygame.draw.circle(
        medium, "white", (medium.width / 2, medium.height / 2), medium.height / 2
    )
    surf.blit(medium, special_flags=pygame.BLEND_RGBA_MULT)
    return surf


def get_it():
    surf = pygame.Surface((SIZE, SIZE), pygame.SRCALPHA)
    middle = SIZE * 0.4
    side = (SIZE - middle) / 2
    pygame.draw.rect(surf, "#008C45", (0, 0, side, SIZE))
    pygame.draw.rect(surf, "#F4F9FF", (side, 0, middle, SIZE))
    pygame.draw.rect(surf, "#CD212A", (side + middle, 0, side, SIZE))
    return make_circle(surf)


def get_en():
    surf = pygame.Surface((SIZE, SIZE), pygame.SRCALPHA)
    white, red, blue = "#FFFFFF", "#C8102E", "#012169"
    big_w, big_r = SIZE * 0.25, SIZE * 0.18
    dg_w, dg_r = int(SIZE * 0.2), int(SIZE * 0.1)
    displacement = SIZE * 0.2
    surf.fill(blue)
    pygame.draw.rect(surf, white, (SIZE / 2 - big_w / 2, 0, big_w, SIZE))
    pygame.draw.line(
        surf, white, (0 - displacement, 0), (SIZE + displacement, SIZE), dg_w
    )
    pygame.draw.line(
        surf, white, (0 - displacement, SIZE), (SIZE + displacement, 0), dg_w
    )
    pygame.draw.line(
        surf, red, (0 - displacement, 0), (SIZE + displacement, SIZE), dg_r
    )
    pygame.draw.line(
        surf, red, (0 - displacement, SIZE), (SIZE + displacement, 0), dg_r
    )
    pygame.draw.rect(surf, white, (0, SIZE / 2 - big_w / 2, SIZE, big_w))
    pygame.draw.rect(surf, red, (0, SIZE / 2 - big_r / 2, SIZE, big_r))
    pygame.draw.rect(surf, red, (SIZE / 2 - big_r / 2, 0, big_r, SIZE))
    return make_circle(surf)


it = get_it()
en = get_en()
pygame.image.save(it, "sito/static/sito/flag_it.png")
pygame.image.save(en, "sito/static/sito/flag_en.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.get_surface().fill("black")
    it = get_it()
    en = get_en()
    win.get_surface().blit(it, (0, 0))
    win.get_surface().blit(en, (it.width, 0))
    win.flip()
