import pygame
import tkinter as tk
from tkinter import simpledialog
import backtracksudoku

matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


pygame.init()

WIDTH = 67
MARGIN = 5

color = (255, 255, 255)


def draw_grid(matrix):
    for row in range(9):
        for column in range(9):
            pygame.draw.rect(win, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + WIDTH) * row + MARGIN, WIDTH, WIDTH])
            if matrix[row][column] != 0:
                font = pygame.font.SysFont('Kameron', 40)
                win.blit(font.render(f"{matrix[row][column]}", True, (0, 0, 0)),
                         [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + WIDTH) * row + MARGIN, WIDTH, WIDTH])


def draw_buttons():
    pygame.draw.rect(win, color, [77, 655, WIDTH, WIDTH])
    font = pygame.font.SysFont('Kameron', 35)
    win.blit(font.render(f"Solve", True, (0, 0, 0)), [77, 680, WIDTH, WIDTH])

    pygame.draw.rect(win, color, [5, 655, WIDTH, WIDTH])
    font = pygame.font.SysFont('Kameron', 35)
    win.blit(font.render(f"New", True, (0, 0, 0)), [5, 680, WIDTH, WIDTH])


win = pygame.display.set_mode((650, 723), pygame.SRCALPHA)
pygame.display.set_caption("Sudoku Solver")
var = True
while var:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos[1] // 72, pos[0] // 72)
            X = pos[1] // 72
            Y = pos[0] // 72
            if X <= 8 and Y <= 8:
                ROOT = tk.Tk()
                ROOT.withdraw()

                x = simpledialog.askstring(title="Test",
                                           prompt="Enter The Value:")
                matrix[X][Y] = int(x)
            elif X == 9 and Y == 1:
                backtracksudoku.solve(matrix)
            elif X == 9 and Y == 0:
                for row in range(9):
                    for column in range(9):
                        matrix[row][column] = 0
    draw_grid(matrix)
    draw_buttons()

    pygame.display.flip()