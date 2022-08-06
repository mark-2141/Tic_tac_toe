from math import inf
import pygame
from pygame.locals import *
import sys
import time

def main():
    #variables
    window_x = 900
    window_y = 900
    sleep_time = 5
    cross = True
    board = [3 * [None], 3 * [None], 3 * [None]]

    pygame.init()

    WHITE = pygame.Color(255, 255, 255)
    GREEN = pygame.Color(0, 255, 0)
    TRANSPARENT = pygame.Color(0, 0, 0, 0)

    pygame.display.set_caption("Tic-Tac-Toe")
    game_display = pygame.display.set_mode((window_x, window_y))
 
    #minimax algorithm has no depth, it is feasible to calculate all positions
    def minimax(board, maximizingPlayer, game_logic, best_row, best_col):

        results = {
            "x":1,
            "Tie":0,
            "o":-1
        }

        if game_logic() != None:
            return (results[game_logic()], best_row, best_col)
        
        if maximizingPlayer:
            value = -inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == None:
                        board[row][col] = 'x'
                        res = minimax(board, False, game_logic, best_row, best_col)[0]
                        if res > value:
                            value = res
                            best_row, best_col = row, col
                        board[row][col] = None
            return (value, best_row, best_col)
        
        else:
            value = inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == None:
                        board[row][col] = 'o'
                        res = minimax(board, True, game_logic, best_row, best_col)[0]
                        if res < value:
                            value = res
                            best_row, best_col = row, col
                        board[row][col] = None
            return (value, best_row, best_col)

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
        board[row][col] = "x"

    def draw_circle(row, col):
        pygame.draw.circle(game_display, WHITE, (window_x*col/3 + window_x/6, window_y*row/3 + window_y/6), min(window_x/10, window_y/10), 3)
        board[row][col] = "o"

    def is_valid_square(row, col):
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
                if board[i][0] == "x":
                    return "x"
                elif board[i][0] == "o":
                    return "o"
        #columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][1] != None:
                if board[0][i] == "x":
                    return "x"
                elif board[0][i] == "o":
                    return "o"
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
                if board[1][1] == "x":
                    return "x"
                elif board[1][1] == "o":
                    return "o"

        if board[0][2] == board[1][1] == board[2][0] and board[1][1] != None:
                if board[1][1] == "x":
                    return "x"
                elif board[1][1] == "o":
                    return "o"
        #draw
        has_none = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    has_none = True
                    continue
        
        if has_none == False:
            return "Tie"

    def is_game_over(game_logic):
        if game_logic() == "x":
            printer('Player ' + str(1) + " won")
            pygame.display.update()
            time.sleep(sleep_time)
            pygame.quit()
            sys.exit()
        if game_logic() == "o":
            printer('Player ' + str(2) + " won")
            pygame.display.update()
            time.sleep(sleep_time)
            pygame.quit()
            sys.exit()
        if game_logic() == "Tie":
            printer("Tie")
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

    first_move = True

    #game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                row, col = user_click()
                if is_valid_square(row, col):
                    if not cross:
                        draw_circle(row, col)
                        cross = True
            pygame.display.update()
            is_game_over(game_logic)
            if cross:
                if first_move:
                    draw_x(0,0)
                    first_move = False
                    cross = False
                else:
                    best_row, best_col = minimax(board, True, game_logic, None, None)[1:]
                    draw_x(best_row, best_col)
                    cross = False    

if __name__ == "__main__":
    main()