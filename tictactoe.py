import pygame
from pygame.locals import *
import sys
import time

def main():
    #variables
    window_x = 900
    window_y = 900
    sleep_time = 5
    #The game is always started by Player 1 with a cross
    cross = True
    board = [3 * [None], 3 * [None], 3 * [None]]

    pygame.init()

    WHITE = pygame.Color(255, 255, 255)
    GREEN = pygame.Color(0, 255, 0)
    TRANSPARENT = pygame.Color(0, 0, 0, 0)

    pygame.display.set_caption("Tic-Tac-Toe")
    game_display = pygame.display.set_mode((window_x, window_y))

    def draw_grid():
        #vertical lines
        pygame.draw.line(game_display, WHITE, (window_x / 3, 0), (window_x / 3, window_y), 3)
        pygame.draw.line(game_display, WHITE, (window_x / 3 * 2 , 0), (window_x / 3 * 2, window_y), 3)
    #horizontal lines
        pygame.draw.line(game_display, WHITE, (0, window_y / 3), (window_x, window_y / 3), 3)
        pygame.draw.line(game_display, WHITE, (0, window_y / 3 * 2), (window_x, window_y/ 3 * 2), 3)

    def draw_x(row, col):
        pygame.draw.line(game_display, WHITE, (col*window_x/3 + window_x/12, row*window_y/3 + window_y/12),
                                              (col*window_x/3 + window_x/4, row*window_y/3 + window_y/4), 3)
        pygame.draw.line(game_display, WHITE, (col*window_x/3 + window_x/12, row*window_y/3 + window_y/4),
                                              (col*window_x/3 + window_x/4, row*window_y/3 + window_y/12), 3)
        board[row][col] = 1

    def draw_circle(row, col):
        pygame.draw.circle(game_display, WHITE, (window_x*col/3 + window_x/6, window_y*row/3 + window_y/6), min(window_x/10, window_y/10), 3)
        board[row][col] = 0

    def is_valid(row, col):
        if board[row][col] == None:
            return True
        else:
            return False

    def user_click():
        # get coordinates of mouse click
        x, y = pygame.mouse.get_pos()
        # get column of mouse click (1-3)
        if(x < window_x / 3):
            col = 0
        elif (x < window_x / 3 * 2):
            col = 1
        elif(x < window_x):
            col = 2
        else:
            col = None
        # get row of mouse click (1-3)
        if(y < window_y / 3):
            row = 0
        elif (y < window_y / 3 * 2):
            row = 1
        elif(y < window_y):
            row = 2
        else:
            row = None
        return(row, col)

    def game_logic():
        #rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != None:
                if board[i][0] == 1:
                    return 1
                elif board[i][0] == 0:
                    return 2
        #columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][1] != None:
                if board[0][i] == 1:
                    return 1
                elif board[0][i] == 0:
                    return 2
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
                if board[1][1] == 1:
                    return 1
                elif board[1][1] == 0:
                    return 2

        if board[0][2] == board[1][1] == board[2][0] and board[1][1] != None:
                if board[1][1] == 1:
                    return 1
                elif board[1][1] == 0:
                    return 2
        #draw
        has_none = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    has_none = True
                    continue
        
        if has_none == False:
            return 3

    def is_game_over(game_logic):
        if game_logic() == 1:
            printer('Player ' + str(1) + " won")
            pygame.display.update()
            time.sleep(sleep_time)
            pygame.quit()
            sys.exit()
        if game_logic() == 2:
            printer('Player ' + str(2) + " won")
            pygame.display.update()
            time.sleep(sleep_time)
            pygame.quit()
            sys.exit()
        if game_logic() == 3:
            printer("Draw")
            pygame.display.update()
            time.sleep(sleep_time)
            pygame.quit()
            sys.exit()

    def printer(text):
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = fontObj.render(text, True, GREEN, TRANSPARENT)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (window_x/2, window_y/18)
        game_display.blit(textSurfaceObj, textRectObj)

    draw_grid()

    #game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                row, col = user_click()
                if is_valid(row, col):
                    if cross:
                        draw_x(row, col)
                        cross = False
                    else:
                        draw_circle(row, col)
                        cross = True
        pygame.display.update()
        is_game_over(game_logic)

if __name__ == "__main__":
    main()