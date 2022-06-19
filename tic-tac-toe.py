from tkinter import *
import pygame

SIZE = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PROPERTY = 360
BOARD = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def createTheGrid(screen):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(i * SIZE + PROPERTY / 4, j * SIZE + PROPERTY / 4, SIZE, SIZE), 2)


def checkWin(player, screen):
    if BOARD[0][0] == player:
        if BOARD[1][0] == player:
            if BOARD[2][0] == player:
                pygame.draw.line(screen, RED, (95, 120), (265, 120), 10)
                pygame.display.update()
                return True
        elif BOARD[0][1] == player:
            if BOARD[0][2] == player:
                pygame.draw.line(screen, RED, (120, 93), (120, 267), 10)
                pygame.display.update()
                return True

    if BOARD[1][1] == player:
        if BOARD[2][2] == player:
            if BOARD[0][0] == player:
                pygame.draw.line(screen, RED, (95, 95), (265, 265), 10)
                pygame.display.update()
                return True
        elif BOARD[1][0] == player:
            if BOARD[1][2] == player:
                pygame.draw.line(screen, RED, (180, 95), (180, 265), 10)
                pygame.display.update()
                return True
        elif BOARD[0][1] == player:
            if BOARD[2][1] == player:
                pygame.draw.line(screen, RED, (95, 180), (265, 180), 10)
                pygame.display.update()
                return True
        elif BOARD[2][0] == player:
            if BOARD[0][2] == player:
                pygame.draw.line(screen, RED, (95, 265), (265, 95), 10)
                pygame.display.update()
                return True
    elif BOARD[2][2] == player:
        if BOARD[2][1] == player:
            if BOARD[2][0] == player:
                pygame.draw.line(screen, RED, (240, 95), (240, 265), 10)
                pygame.display.update()
                return True
        elif BOARD[1][2] == player:
            if BOARD[0][2] == player:
                pygame.draw.line(screen, RED, (95, 240), (265, 240), 10)
                pygame.display.update()
                return True
    else:
        return False


def checkCollision(x, y, player):
    if x in range(90, 270) and y in range(90, 270):
        if x in range(90, 150):
            if y in range(90, 150):
                if BOARD[0][0] == "o" or BOARD[0][0] == "x":
                    return False
                else:
                    BOARD[0][0] = player
                    return True
            elif y in range(151, 210):
                if BOARD[0][1] == "o" or BOARD[0][1] == "x":
                    return False
                else:
                    BOARD[0][1] = player
                    return True
            else:
                if BOARD[0][2] == "o" or BOARD[0][2] == "x":
                    return False
                else:
                    BOARD[0][2] = player
                    return True
        elif x in range(151, 210):
            if y in range(90, 150):
                if BOARD[1][0] == "o" or BOARD[1][0] == "x":
                    return False
                else:
                    BOARD[1][0] = player
                    return True
            elif y in range(151, 210):
                if BOARD[1][1] == "o" or BOARD[1][1] == "x":
                    return False
                else:
                    BOARD[1][1] = player
                    return True
            else:
                if BOARD[1][2] == "o" or BOARD[1][2] == "x":
                    return False
                else:
                    BOARD[1][2] = player
                    return True
        else:
            if y in range(90, 150):
                if BOARD[2][0] == "o" or BOARD[2][0] == "x":
                    return False
                else:
                    BOARD[2][0] = player
                    return True
            elif y in range(151, 210):
                if BOARD[2][1] == "o" or BOARD[2][1] == "x":
                    return False
                else:
                    BOARD[2][1] = player
                    return True
            else:
                if BOARD[2][2] == "o" or BOARD[2][2] == "x":
                    return False
                else:
                    BOARD[2][2] = player
                    return True
    else:
        return False


def newGame(screen):
    pygame.time.delay(2000)
    screen.fill(BLACK)
    my_font = pygame.font.SysFont("monospace", 40)
    text_surface = my_font.render("Tic Tac Toe", True, WHITE)
    screen.blit(text_surface, (50, 30))
    createTheGrid(screen)
    for i in range(3):
        for j in range(3):
            BOARD[i][j] = 0
    pygame.display.flip()


def boardFull():
    num = 0
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] == "x" or BOARD[i][j] == "o":
                num += 1
    if num == 9:
        return True
    return False


def placeO(screen, x, y):
    if checkCollision(x, y, "o"):
        pygame.draw.circle(screen, WHITE, [x, y], 20, 6)
        pygame.display.update()
        if checkWin("o", screen):
            pygame.time.delay(500)
            screen.fill(BLACK)
            font1 = pygame.font.SysFont('monospace', 24)
            text_game_over = font1.render("Well done player O!", True, WHITE)
            screen.blit(text_game_over, (40, 160))
            pygame.display.flip()
            pygame.time.delay(2000)
            newGame(screen)
        if boardFull():
            newGame(screen)
        return True
    return False


def placeX(screen, x, y):
    if checkCollision(x, y, "x"):
        pygame.draw.line(screen, WHITE, (x - 18, y - 18), (x + 18, y + 18), 8)
        pygame.draw.line(screen, WHITE, (x - 18, y + 18), (x + 18, y - 18), 8)
        pygame.display.update()
        if checkWin("x", screen):
            pygame.time.delay(500)
            screen.fill(WHITE)
            font1 = pygame.font.SysFont('monospace', 20)
            text_game_over = font1.render("Player X u are amazing!", True, BLACK)
            screen.blit(text_game_over, (40, 160))
            pygame.display.flip()
            pygame.time.delay(2000)
            newGame(screen)
        if boardFull():
            newGame(screen)
        return True
    return False


def startTheGame():
    player = 0

    pygame.init()
    screen = pygame.display.set_mode((PROPERTY, PROPERTY))
    my_font = pygame.font.SysFont("monospace", 40)
    pygame.display.set_caption('Tic Tac Toe by xtrdmnrmnd')
    text_surface = my_font.render("Tic Tac Toe", True, WHITE)
    screen.blit(text_surface, (50, 30))
    createTheGrid(screen)
    text_xtrdnrmnd = pygame.font.SysFont('monospace', 20).render("Made by xtrdnrmnd, 2022", True, WHITE)
    screen.blit(text_xtrdnrmnd, (45, 340))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if player == 0:
                    if placeX(screen, x, y):
                        player = 1
                    else:
                        placeX(screen, x, y)
                else:
                    if placeO(screen, x, y):
                        player = 0
                    else:
                        placeO(screen, x, y)

            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    startTheGame()
