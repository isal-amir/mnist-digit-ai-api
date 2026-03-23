import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Ied Mubarak 1447 H")

BLACK = (0, 0, 0)
GREEN = (0, 255, 120)

font = pygame.font.SysFont("courier", 12, bold=True)

# ASCII template huruf (besar)
ascii_text = [

"                  $$$$$$$                ",
"              $$$   $$             $        ",
"            $$   $$               $$$         ",
"           $$   $$            $$$$$$$$$$$            ",
"           $$   $$              $$  $$            ",
"            $$   $$            $$    $$           ",
"              $$$   $$        $        $           ",
"                  $$$$$$$                         ",
"",
"                             $                   ",
"                            $$$                  ",
"                             $                   ",
"",
"  $$   $$    $$$$$    $$$$$$   $$$$$$   $$     $$ ",
"  $$   $$   $$   $$   $$   $$  $$   $$    $$  $$ ",
"  $$$$$$$   $$$$$$$   $$$$$$   $$$$$$       $$ ",
"  $$   $$   $$   $$   $$       $$           $$  ",
"  $$   $$   $$   $$   $$       $$           $$  ",
"",
" $$$$    $$$$$$$  $$$$ ",
"  $$     $$       $$  $$   ",
"  $$     $$$$$    $$   $$   ",
"  $$     $$       $$  $$   ",
" $$$$    $$$$$$$  $$$$ ",
"",
" $$       $$  $$    $$  $$$$$$     $$$$$    $$$$$     $$$$$   $$  $$    ",
" $$$     $$$  $$    $$  $$   $$   $$   $$   $$   $$  $$   $$  $$ $$      ",
" $$ $$ $$ $$  $$    $$  $$$$$$$   $$$$$$$   $$$$$    $$$$$$$  $$$$        ",
" $$  $$$  $$  $$    $$  $$   $$   $$   $$   $$ $$    $$   $$  $$ $$      ",
" $$   $   $$   $$$$$$   $$$$$$    $$   $$   $$   $$  $$   $$  $$  $$     ",
"",
"  $$$       $$$       $$$   $$$$$$$$   $$    $$       ",
" $ $$     $$ $$     $$ $$        $$    $$    $$        ",
"   $$   $$$$$$$   $$$$$$$       $$     $$$$$$$$        ",
"   $$        $$        $$      $$      $$    $$        ",
"   $$        $$        $$     $$       $$    $$        "
]

# Ubah semua karakter non-spasi jadi $
ascii_dollar = []
for line in ascii_text:
    new_line = ""
    for ch in line:
        if ch == " ":
            new_line += " "
        else:
            new_line += "$"
    ascii_dollar.append(new_line)

clock = pygame.time.Clock()
time = 0

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gambar ASCII dengan efek gelombang
    for row_idx, line in enumerate(ascii_dollar):
        for col_idx, char in enumerate(line):
            if char == "$":
                # posisi dasar
                x = col_idx * 12 + 50
                y = row_idx * 18 + 50

                # efek wave
                offset = math.sin(time + col_idx * 0.3) * 5

                # efek fade warna
                color_intensity = (math.sin(time + col_idx * 0.2) + 1) / 2
                color = (
                    0,
                    int(150 + 105 * color_intensity),
                    int(80 + 175 * color_intensity)
                )

                text_surface = font.render("$", True, color)
                screen.blit(text_surface, (x, y + offset))

    time += 0.05

    pygame.display.flip()
    clock.tick(60)